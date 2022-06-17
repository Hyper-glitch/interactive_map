""" Module for custom management commands """
import uuid

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Place, Image


class Command(BaseCommand):
    help = 'Add a new places to DataBase'

    def add_arguments(self, parser):
        parser.add_argument('places_urls', type=str)

    def handle(self, *args, **options):
        """ Read file with urls and create places with json info."""
        path = options['places_urls']

        with open(path) as places_urls:
            urls = places_urls.readlines()

        for url in urls:
            response = requests.get(url=url.rstrip('\n'))
            response.raise_for_status()
            payload = response.json()
            place, created = Place.objects.get_or_create(
                title=payload['title'],
                defaults={
                    'description_short': payload['description_short'],
                    'description_long': payload['description_long'],
                    'latitude': payload['coordinates']['lat'],
                    'longitude': payload['coordinates']['lng'],
                }
            )
            for img in place['imgs']:
                position = 1
                save_place_img(img_url=img, place=place, position=position)
                position += 1


def save_place_img(img_url, place, position):
    """ Send request for getting img content and save it in FileField. """
    filename = str(uuid.uuid4())
    response = requests.get(img_url)
    response.raise_for_status()
    content = ContentFile(response.content)
    img = Image.objects.create(place=place, name=filename, position=position)
    img.image.save(filename, content, save=True)

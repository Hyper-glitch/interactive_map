import uuid

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Place, Image


class Command(BaseCommand):
    help = 'Add a new places to DataBase'

    def add_arguments(self, parser):
        parser.add_argument('places_urls', nargs='+', type=str)

    def handle(self, *args, **options):
        path = options['places_urls'][0]

        with open(path) as places_urls:
            urls = places_urls.readlines()

            for url in urls:
                response = requests.get(url=url.rstrip('\n'))
                response.raise_for_status()
                place = response.json()
                place_obj = Place.objects.get_or_create(
                    title=place['title'], description_short=place['description_short'],
                    description_long=place['description_long'], coordinates=place['coordinates'],
                )
                for img in place['imgs']:
                    position = 1
                    save_place_img(img_url=img, place=place_obj[0], position=position)
                    position += 1


def save_place_img(img_url, place, position):
    filename = str(uuid.uuid4())
    response = requests.get(img_url)
    response.raise_for_status()
    content = ContentFile(response.content)
    img = Image.objects.create(place=place, name=filename, position=position)
    img.image.save(filename, content, save=True)

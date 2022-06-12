import uuid

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Place, Image


class Command(BaseCommand):
    help = 'Add a new place to DataBase'

    def add_arguments(self, parser):
        parser.add_argument('json_url', nargs='+', type=str)

    def handle(self, *args, **options):
        url = options['json_url'][0]
        response = requests.get(url=url)
        response.raise_for_status()
        place = response.json()
        place_obj = Place.objects.get_or_create(
            title=place['title'], description_short=place['description_short'],
            description_long=['description_long'], coordinates=place['coordinates'],
        )
        for img in place['imgs']:
            position = 1
            save_place_img(img_url=img, place=place_obj[0], position=position)
            position += 1


def save_place_img(img_url, place, position):
    filename = str(uuid.uuid4())
    response = requests.get(img_url)
    response.raise_for_status()
    Image.objects.create(place=place, name=filename, image=ContentFile(response.content), position=position)

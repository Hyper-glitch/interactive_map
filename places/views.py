from django.shortcuts import render
from django.core import serializers
from places.models import Place


def index(request):
    data = {
        "type": "FeatureCollection",
        "features": get_json_places(request),
    }
    return render(request, 'index.html', context=data)


def get_json_places(request):
    places = Place.objects.all()
    features = []
    place_id = 0

    for place in places:
        images = place.images.all()
        detailed_places_info = {
            "title": place.title,
            "imgs": [image.image.url for image in images],
            "description_short": place.description_short,
            "description_long": place.description_long,
            "coordinates": place.coordinates,
        }

        place_info = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": place.get_coordinates()
            },
            "properties": {
                "title": place.title,
                "placeId": place_id,
                "detailsUrl": detailed_places_info
            }
        }
        features.append(place_info)
        place_id += 1

    return features

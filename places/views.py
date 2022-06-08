from django.http import JsonResponse
from django.shortcuts import render
import json
from places.models import Place


def index(request):
    data = {
        "type": "FeatureCollection",
        "features": get_json_places(request),
    }
    return render(request, 'index.html', context={"data": data})


def get_json_places(request):
    places = Place.objects.all()
    features = []
    place_id = 0

    for place in places:
        place_info = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": place.get_coordinates()
            },
            "properties": {
                "title": place.title,
                "placeId": place_id,
                "detailsUrl": f"get_json_place/{place.pk}"
            }
        }
        features.append(place_info)
        place_id += 1

    return features


def get_json_place(request, place_pk):
    place = Place.objects.get(pk=place_pk)
    images = place.images.all()
    detailed_places_info = {
        "title": place.title,
        "imgs": [image.image.url for image in images],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": place.coordinates,
    }
    return JsonResponse(detailed_places_info, safe=False)

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from places.models import Place


def index(request):
    data = {
        "type": "FeatureCollection",
        "features": create_places_info(request),
    }
    return render(request, 'index.html', context={"data": data})


def create_places_info(request):
    places = Place.objects.all()
    features = []
    place_id = 0

    for place in places:
        place_info = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.longitude, place.latitude]
            },
            "properties": {
                "title": place.title,
                "placeId": place_id,
                "detailsUrl": f"{reverse('get_json_place', args=(place.pk,))}"
            }
        }
        features.append(place_info)
        place_id += 1

    return features


def get_json_place(request, place_pk):
    place = get_object_or_404(Place, pk=place_pk)
    images = place.images.all()
    detailed_places_info = {
        "title": place.title,
        "imgs": [image.image.url for image in images],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": [place.longitude, place.latitude],
    }
    return JsonResponse(detailed_places_info, safe=False)

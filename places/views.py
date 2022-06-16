from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from places.models import Place


def index(request):
    places_geojson = {
        "type": "FeatureCollection",
        "features": create_places_geojson(request),
    }
    return render(request, 'index.html', context={"places_geojson": places_geojson})


def create_places_geojson(request):
    places = Place.objects.all()
    features = []

    for index, place in enumerate(places):
        places_geojson = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.longitude, place.latitude]
            },
            "properties": {
                "title": place.title,
                "placeId": index,
                "detailsUrl": f"{reverse('get_json_place', args=(place.pk,))}"
            }
        }
        features.append(places_geojson)

    return features


def get_json_place(request, place_pk):
    place = get_object_or_404(Place, pk=place_pk)
    images = place.images.all()
    serialized_place = {
        "title": place.title,
        "imgs": [image.image.url for image in images],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": [place.longitude, place.latitude],
    }
    return JsonResponse(serialized_place, safe=False)

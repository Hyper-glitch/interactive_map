from django.db import models
from jsonfield import JSONField


class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.CharField(max_length=500)
    description_long = models.TextField()
    coordinates = JSONField()

    def __str__(self):
        return self.title

    def get_coordinates(self):
        coordinates = [*self.coordinates.values()]
        return coordinates


class Image(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='places_pics')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f'{self.pk} {self.name}'

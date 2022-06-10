from django.db import models
from tinymce.models import HTMLField
from jsonfield import JSONField


class Place(models.Model):

    class Meta:
        ordering = ["order"]

    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )
    title = models.CharField(max_length=200)
    description_short = models.CharField(max_length=500)
    description_long = HTMLField()
    coordinates = JSONField()

    def __str__(self):
        return self.title

    def get_coordinates(self):
        coordinates = [*self.coordinates.values()]
        return coordinates


class Image(models.Model):
    class Meta:
        ordering = ["position"]

    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='places_pics')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')
    position = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.position} {self.name}'

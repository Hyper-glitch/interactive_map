from django.db import models
from jsonfield import JSONField
from tinymce.models import HTMLField


class Place(models.Model):
    order = models.PositiveIntegerField(default=1)
    title = models.CharField(max_length=200)
    description_short = models.TextField(blank=True, null=True)
    description_long = HTMLField(blank=True, null=True)
    coordinates = JSONField()

    class Meta:
        ordering = ['order']
        unique_together = ['title', 'id']

    def __str__(self):
        return self.title

    def get_coordinates(self):
        coordinates = [*self.coordinates.values()]
        return coordinates


class Image(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='places_pics', null=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')
    position = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["position"]

    def __str__(self):
        return f'{self.position} {self.name}'

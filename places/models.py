from django.db import models
from jsonfield import JSONField


class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.CharField(max_length=500)
    description_long = models.TextField()
    coordinates = JSONField()

    def __str__(self):
        return self.title

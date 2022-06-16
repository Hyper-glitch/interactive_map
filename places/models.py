from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    order = models.PositiveIntegerField(default=1, verbose_name='Последовательность')
    title = models.CharField(max_length=200, unique=True, verbose_name='Название места')
    description_short = models.TextField(blank=True, verbose_name='Короткое описание')
    description_long = HTMLField(blank=True, verbose_name='Основное описание')
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')

    class Meta:
        ordering = ['order']
        unique_together = ['title', 'id']
        verbose_name = 'Интересное место'
        verbose_name_plural = 'Интересные места'

    def __str__(self):
        return self.title


class Image(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название изображения')
    image = models.ImageField(upload_to='places_pics', null=True, verbose_name='Изображение')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')
    position = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['position']
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return f'{self.position} {self.name}'

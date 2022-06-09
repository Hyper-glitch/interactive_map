from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminMixin
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ('get_preview',)

    def get_preview(self, image):
        return mark_safe(f'<img src="{image.image.url}" width="300" height="200" />')


@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [ImageInline]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass

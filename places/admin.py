from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from .models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ('get_preview',)
    extra = 0

    def get_preview(self, image):
        return format_html('<img src="{}" width="300" height="200" />', image.image.url)


@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    search_fields = ['title']
    inlines = [ImageInline]

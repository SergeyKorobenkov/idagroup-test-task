from django.contrib import admin

from .models import BaseImage


class BaseImageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'image',
        'url',
    )
    empty_value_display = '-пусто-'


admin.site.register(BaseImage, BaseImageAdmin)
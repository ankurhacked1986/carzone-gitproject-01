from django.contrib import admin
from .models import Car
from django.utils.html import format_html

# Register your models here.

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src = "{}" width = "100" style = "border-radius: 50px;"/>'.format(object.car_photo.url))
    thumbnail.short_description = 'photo'

    list_display = ('id','car_name','thumbnail','color','price','is_featured')
    list_display_links = ('id','car_name','thumbnail')
    list_editable = ('is_featured','price','color')
    search_fields = ('car_name','price','color')
    list_filter = ('price',)

admin.site.register(Car,CarAdmin)
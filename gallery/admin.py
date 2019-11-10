from django.contrib import admin
from .models import Gallery, Image


class ImageAdmin(admin.ModelAdmin):
    model = Image




class GalleryAdmin(admin.ModelAdmin):
    model = Gallery


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Image, ImageAdmin)
# Register your models here.

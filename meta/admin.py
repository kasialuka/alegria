from django.contrib import admin
from .models import Meta
# Register your models here.

class MetaAdmin(admin.ModelAdmin):

    class Meta:
        verbose_name_plural = 'meta'

admin.site.register(Meta, MetaAdmin)

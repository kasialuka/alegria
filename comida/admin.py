from django.contrib import admin
from .models import Food, FoodCategory



class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)

class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'show' )




admin.site.register(Food, FoodAdmin)
admin.site.register(FoodCategory, FoodCategoryAdmin)




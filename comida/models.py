from django.db import models

# Create your models here.

class FoodCategory(models.Model):
    category = models.CharField(max_length=128 )



    def __str__(self):
        return self.category

class Food(models.Model):
    category = models.ForeignKey(FoodCategory, null=True, on_delete=models.CASCADE)
    show = models.BooleanField(default=True)
    price = models.FloatField()
    name = models.CharField(max_length=256, blank=False)
    short_description = models.TextField(max_length=256)
    description = models.TextField(max_length=1024)
    image_01  = models.ImageField(upload_to='food_images/', blank=True)
    image_02 = models.ImageField(upload_to='food_images/',blank=True)
    image_03= models.ImageField(upload_to='food_images/', blank=True)
    image_04 =models.ImageField(upload_to='food_images/', blank=True)


    def __str__(self):
        return self.name





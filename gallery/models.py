from django.db import models

# Create your models here.

class Image(models.Model):
    title = models.CharField(max_length=256)
    alt = models.CharField(max_length=256)
    image = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return self.title

class Gallery(models.Model):
    gallery_name= models.CharField(max_length=256)
    images = models.ManyToManyField(Image)

    def __str__(self):
        return self.gallery_name

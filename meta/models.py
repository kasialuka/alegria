from django.db import models

# Create your models here.


class Meta(models.Model):
    author = models.TextField(max_length=512)
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=512)
    keywords = models.TextField(max_length=512)

    def __str__(self):
        return self.title+'_'+str(self.pk)

    class Meta:
        verbose_name_plural = 'meta'



    class Meta:
        verbose_name_plural = 'meta'




from django.db import models
from info.models import CompanyData


class Header(models.Model):
    title = models.CharField(max_length=512)
    main_image = models.ImageField(upload_to='mainpage/')


class Footer(models.Model):
    name = models.CharField(max_length=50, default='test')
    company_data = models.ForeignKey(CompanyData, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

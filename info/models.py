from django.db import models

class AboutUs(models.Model):
    description_title = models.CharField(max_length=256)
    company_description = models.TextField(blank=True)
    about_us_image_01 = models.ImageField(upload_to='about_us')
    about_us_image_02 =  models.ImageField(upload_to='about_us', blank=True)
    about_us_image_03 = models.ImageField(upload_to='about_us', blank=True)

    def image_tag(self):
        im  = self.about_us_image_01.upload_to
        return f'<img src="dupa{im}" />'
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True




    class Meta:
        verbose_name_plural = 'About Us'



class StaffPerson(models.Model):
    first_name = models.CharField(max_length=128, blank=True)
    second_name = models.CharField(max_length=128, blank=True)
    nickname = models.CharField(max_length=128, blank=True)
    few_words_about = models.TextField(max_length=1024)
    face = models.ImageField(upload_to='StaffPerson/')
    staff = models.ForeignKey(AboutUs, on_delete=models.CASCADE, blank=True, null=True)

    #imported_person = models.ForeignKey()

    def __str__(self):
        return self.first_name+self.second_name


class CompanyData(models.Model):
    company_name = models.CharField(max_length=256)
    adress_line_1 = models.CharField(max_length=256)
    adress_line_2 = models.CharField(max_length=256, blank=True)
    adress_line_3 = models.CharField(max_length=256, blank=True)
    telephone = models.BigIntegerField(blank=True)
    telephone_mobile = models.BigIntegerField(blank=True)
    e_mail = models.EmailField()

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name_plural = 'Company Data'




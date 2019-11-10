from django.contrib import admin
from .models import StaffPerson, AboutUs, CompanyData




class StaffPersonAdmin(admin.StackedInline):
    model = StaffPerson





class CompanyDataAdmin(admin.ModelAdmin):
    pass

class AboutUsAdmin(admin.ModelAdmin):
    # list_display = ('description_title',)
    fields = ['image_tag', 'description_title', 'company_description', 'about_us_image_01', 'about_us_image_02', 'about_us_image_03']
    readonly_fields = ('image_tag',)

    inlines = [StaffPersonAdmin]



# admin.site.register(StaffPerson, StaffPersontAdmin)

admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(CompanyData, CompanyDataAdmin)





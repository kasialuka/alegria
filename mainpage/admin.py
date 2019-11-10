from django.contrib import admin
from mainpage.models import Header, Footer


class HeaderAdmin(admin.ModelAdmin):
    pass

class FooterAdmin(admin.ModelAdmin):
    pass

admin.site.register(Header, HeaderAdmin)
admin.site.register(Footer, FooterAdmin)

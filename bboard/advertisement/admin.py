from django.contrib import admin
from advertisement.models import Advertisement, Rubrik, Author, Advertisement_type1


# Register your models here.
#@admin.register(Advertisement, Rubrik, Author, Advertisement_type1)
# @admin.register(Rubrik)
# @admin.register(Author)

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    pass

admin.site.register( Advertisement,AdvertisementAdmin)
admin.site.register(Rubrik,AdvertisementAdmin)
admin.site.register(Author,AdvertisementAdmin)
admin.site.register(Advertisement_type1,AdvertisementAdmin)
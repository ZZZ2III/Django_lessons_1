from django.contrib import admin
from advertisement.models import Advertisement, Rubrik, Author, Advertisement_type1


# Register your models here.
# @admin.register(Advertisement, Rubrik, Author, Advertisement_type1)
# @admin.register(Rubrik)
# @admin.register(Author)

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['description']
    pass

class RubrickAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    pass

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields=['name']
    pass

class Adv_1Admin(admin.ModelAdmin):
    list_display = ['id', 'name']
    pass

admin.site.register(Advertisement, AdvertisementAdmin)
admin.site.register(Rubrik, RubrickAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Advertisement_type1, Adv_1Admin)

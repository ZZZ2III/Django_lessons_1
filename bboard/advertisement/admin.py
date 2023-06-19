from django.contrib import admin
from advertisement.models import Advertisement, Rubrik, Author, Advertisement_type1


# Register your models here.
@admin.register(Advertisement, Rubrik, Author, Advertisement_type1)
# @admin.register(Rubrik)
# @admin.register(Author)

class AdvertisementAdmin(admin.ModelAdmin):
    pass

# class RubrikAdmin(admin.ModelAdmin):
#     pass
#
# class AuthorAdmin(admin.ModelAdmin):
#     pass
#
# class Advertisement_type1Admin(admin.ModelAdmin):
#     pass

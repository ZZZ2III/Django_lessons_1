from django.contrib import admin
from app_library.models import Publisher


# Register your models here.
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'city']
    pass


admin.site.register(Publisher, PublisherAdmin)

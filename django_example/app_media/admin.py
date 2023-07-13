from django.contrib import admin
from app_media.models import File
# Register your models here.
class FilterAdmin(admin.ModelAdmin):
    list_display = ('id','created_at')

admin.site.register(File,FilterAdmin)
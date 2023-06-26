from django.contrib import admin
from app_profiles.models import User,Advertisement
# Register your models here.
@admin.register(User,Advertisement)

class AppAdmin(admin.ModelAdmin):
    pass
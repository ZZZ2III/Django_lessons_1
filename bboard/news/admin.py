from django.contrib import admin
from news.models import NewsModel,CommentsModel
# Register your models here.
@admin.register(NewsModel,CommentsModel)

class NewsAdmin(admin.ModelAdmin):
    pass
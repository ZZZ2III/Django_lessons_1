from django.contrib import admin
from news.models import NewsModel, CommentsModel


# Register your models here.
# @admin.register(NewsModel,CommentsModel)

class CommsInline(admin.TabularInline):
    model = CommentsModel


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'content']
    inlines = [CommsInline]
    pass


class CommentsAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']

    pass


admin.site.register(NewsModel, NewsAdmin)
admin.site.register(CommentsModel, CommentsAdmin)

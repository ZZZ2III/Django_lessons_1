from django.contrib import admin
from news.models import NewsModel, CommentsModel


# Register your models here.
# @admin.register(NewsModel,CommentsModel)

class CommsTabularInline(admin.TabularInline):
    model = CommentsModel


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_created', 'flag_active', 'status']# Показывает что отображать в админке вместо объекта
    list_filter = ['flag_active']# Фильрация по выбранному столбцу
    inlines = [CommsTabularInline]# Удобное отображение добавление новых записей в модель TabularInline или StackedInline
    actions = ['make_active', 'make_inactive']# Регистрация собственных функций

    def make_active(self,request,queryset):
        queryset.update(status='a')

    def make_inactive(self, request, queryset):
        queryset.update(status='i')

    make_active.short_description = 'Сделать новость активной'
    make_inactive.short_description = 'Сделать новость неактивной'

class CommentsAdmin(admin.ModelAdmin):
    list_display = ['name','text']
    list_filter = ['name']
    search_fields = ['name', 'text']
    actions = ['del_by_admin']

    def del_by_admin(self,request,queryset):
        queryset.update(text = 'Удалено администратором')

    del_by_admin.short_description = 'Удалить комментарий'


admin.site.register(NewsModel, NewsAdmin)
admin.site.register(CommentsModel, CommentsAdmin)

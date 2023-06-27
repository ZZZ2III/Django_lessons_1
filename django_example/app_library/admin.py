from django.contrib import admin
from app_library.models import Publisher, Authors, Book


# Register your models here.
class BookInLine(admin.StackedInline):
    model = Book


class PublisherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'city']
    list_filter = ['is_active', 'city']
    inlines = [BookInLine]
    pass


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name']
    # list_filter = ['id', 'first_name', 'last_name']
    search_fields = ['first_name', 'last_name', 'biography']
    fieldsets = (
        (
            "Основные сведения", {
                'fields': ('first_name', 'second_name', 'last_name', 'country', 'city')
            }),
        (
            'Биографические сведения', {
                'fields': ('university', 'birth_date', 'biography'),
                'description': 'Различные данные из биографии автора',
                'classes':['collapse']
            }
        ),
        (
            'Контакты', {
                'fields': ('email', 'phone', 'personal_page', 'facebook', 'twitter'),
                'description':'Как связаться с автором'

            }
        )
    )


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'publisher']


admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Authors, AuthorAdmin)
admin.site.register(Book, BookAdmin)

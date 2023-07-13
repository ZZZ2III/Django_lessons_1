from django.contrib import admin
from app_goods.models import Item, Goods, GoodsHw


# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ('code', 'price')


class GoodsAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'price')


class GoodsHwAdmin(admin.ModelAdmin):
    list_display = ('title', 'code')

admin.site.register(GoodsHw,GoodsHwAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Goods, GoodsAdmin)

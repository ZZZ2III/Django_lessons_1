from django.contrib import admin
from app_goods.models import Item,Goods
# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ('code', 'price')

class GoodsAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'price')

admin.site.register(Item,ItemAdmin)
admin.site.register(Goods,GoodsAdmin)
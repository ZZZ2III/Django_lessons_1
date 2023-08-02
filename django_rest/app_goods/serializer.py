from rest_framework import serializers
from app_goods.models import Item


# class ItemSerializer(serializers.Serializer): Урок 13.3
#     name = serializers.CharField(max_length=200)
#     description = serializers.CharField(allow_blank=True)
#     weight = serializers.FloatField(min_value=0)
#     group = serializers.CharField(max_length=200,allow_blank=True)

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'weight']


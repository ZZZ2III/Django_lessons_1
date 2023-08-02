from django.shortcuts import render
from app_goods.models import Item
from django.http import JsonResponse
from app_goods.serializer import ItemSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
# Возврат json Средствами разработки Джанго
# def items_list(request):
#     if request.method == 'GET':
#         Items_for_sale = [
#             Item(
#                 name='Кофеварка',
#                 description='Варит кофе',
#                 weight=100
#             ),
#             Item(
#                 name='Беспроводные наушники',
#                 description='Проецируют звук в уши',
#                 weight=150
#             )
#         ]
#         return JsonResponse([item.to_dict() for item in Items_for_sale], safe=False)#, encoder='utf-8')


def items_list(request):
    if request.method == 'GET':
        Items_for_sale = [
            Item(
                name='Кофеварка',
                description='Варит кофе',
                weight=100
            ),
            Item(
                name='Беспроводные наушники',
                description='Проецируют звук в уши',
                weight=150
            )
        ]
        return JsonResponse(ItemSerializer(Items_for_sale, many=True).data, safe=False)


def items_list_groups(request):
    if request.method == 'GET':
        Items_for_sale = [
            Item(
                name='Кофеварка',
                description='Варит кофе',
                weight=100,
                group='техника'
            ),
            Item(
                name='Беспроводные наушники',
                description='Проецируют звук в уши',
                weight=150,
                group='техника'
            ),
            Item(
                name='Диван',
                description='очень мягкий и удобный',
                weight=150,
                group='Мебель'
            )
        ]
        mass_for_groups = []
        for i in Items_for_sale:
            mass_for_groups.append(i.group)

        return JsonResponse({'groups': mass_for_groups}, safe=False)


class ItemList(APIView):
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        #print(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ItemGroupList(APIView):
    def get(self,request):
        pass

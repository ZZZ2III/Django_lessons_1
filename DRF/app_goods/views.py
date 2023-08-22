from rest_framework.mixins import ListModelMixin, CreateModelMixin
from app_goods.models import Item
from app_goods.serializers import ItemSerializer
from rest_framework.generics import GenericAPIView


class ItemList(ListModelMixin, CreateModelMixin, GenericAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.all()
        item_name = self.request.query_params.get('name')
        if item_name:
            queryset = queryset.filter(name=item_name)
        return queryset

    def get(self, request):
        return self.list(request)

    def post(self, request, format=None):
        return self.create(request)

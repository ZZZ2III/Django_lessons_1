from _csv import reader
from decimal import Decimal
from django.shortcuts import render
from app_goods.models import Item, Goods
from app_goods.forms import UploadPriceForm
from django.http import HttpResponse
from django.core.exceptions import ValidationError


# Create your views here.

def item_list(request):
    items = Item.objects.all()
    return render(request, 'app_goods/items_list.html', context={'items_list': items})


def update_prices(request):
    if request.method == "POST":
        upload_price_form = UploadPriceForm(request.POST, request.FILES)
        if upload_price_form.is_valid():
            file_name = request.FILES['file'].name
            if file_name[-3:] == 'csv':
                price_file = upload_price_form.cleaned_data['file'].read()
                price_str = price_file.decode('utf-8').split('\n')
                csv_reader = reader(price_str, delimiter=",", quotechar='"')
                for row in csv_reader:
                    Item.objects.filter(code=row[0]).update(price=Decimal(row[1]))
                return HttpResponse(content='Цены были успешно обновлены', status=200)
            else:
                raise ValidationError("Вы должны загружать только csv файлы")
    else:
        upload_price_form = UploadPriceForm()

    context = {
        'form': upload_price_form
    }
    return render(request, 'app_goods/upload_price_file.html', context=context)


def goods_list(request):
    goods = Goods.objects.all()
    return render(request, 'homework/goods.html', context={'goods_list': goods})


def update_goods(request):
    if request.method == "POST":
        upload_goods_form = UploadPriceForm(request.POST, request.FILES)
        if upload_goods_form.is_valid():
            price_file = upload_goods_form.cleaned_data['file'].read()
            price_str = price_file.decode('utf-8').split('\n')
            print(f"Приведенные знаечения { price_file.decode('utf-8')}")
            reader_1 = reader(price_str, delimiter=":", quotechar='"')
            for row in reader_1:
                print(row)
                Goods.objects.filter(code=row[0]).update(price=Decimal(row[1]))
            return HttpResponse(content='Все распарсилось и обновилось', status=200)

    else:
        upload_goods_form = UploadPriceForm()

    context = {
        'goodsform': upload_goods_form
    }

    return render(request, 'homework/goods_update.html', context=context)

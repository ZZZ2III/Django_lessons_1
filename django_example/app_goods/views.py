from _csv import reader
from decimal import Decimal

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from app_goods.models import Item, Goods, GoodsHw
from app_goods.forms import UploadPriceForm
from django.http import HttpResponse
from django.core.exceptions import ValidationError
import datetime


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
            # print(f"Приведенные знаечения {price_file.decode('utf-8')}")  # Перевод в человеческий вид
            reader_1 = reader(price_str, delimiter=":", quotechar='"')
            updated_list = []
            eror_list = []
            for row in reader_1:

                v = Goods.objects.filter(code=row[0]).update(price=Decimal(row[1]))
                if not v:
                    eror_list.append(row)
                if v == 1:
                    print(row)
                    updated_list.append(row)
            code_list = []
            for i in eror_list:
                code_list.append(i[0])
            content = f'Количество обновленных товаров {len(updated_list)}, количество необновленных товаров {len(eror_list)}, Артикулы,которых не было {code_list} '
            return HttpResponse(content=content, status=200)

    else:
        upload_goods_form = UploadPriceForm()

    context = {
        'goodsform': upload_goods_form
    }

    return render(request, 'homework/goods_update.html', context=context)


def update_goods_with_saving(request):
    if request.method == "POST":
        update_goods_form = UploadPriceForm(request.POST, request.FILES)
        if update_goods_form.is_valid():
            # update_goods_form.save()
            file = request.FILES['file']
            price_file = update_goods_form.cleaned_data['file'].read()
            decoded = price_file.decode('utf-8').split('\n')
            readed = reader(decoded, delimiter=':', quotechar='"')
            recent_filename = file.name
            new_filename = str(datetime.datetime.now().strftime('%d%m%y-%H-%M-%S')) + f'_{recent_filename}'

            fs = FileSystemStorage()
            filename = fs.save(new_filename, file)
            # file_url = fs.url(filename)
            for row in readed:
                GoodsHw.objects.filter(code=row[0]).update(price=Decimal(row[1]))
                GoodsHw.objects.filter(code=row[0]).update(file=filename)
            return redirect('/')
    else:
        upload_goods_form = UploadPriceForm()

    return render(request, 'app_goods/update_and_save.html', context={'form': upload_goods_form})


def goods_list_hw(request):
    goods = GoodsHw.objects.all()
    return render(request, 'homework/goods.html', context={'goods_list': goods})

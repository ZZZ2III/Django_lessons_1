from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
import random


# Create your views here.

def advertisement_list(request, *args, **kwargs):
    listq = ['Мастер на час', 'Выведение из запоя', 'Услоги экскаватора погрузчика', "Услуги кошки"]
    return render(request, 'advertisement/advertisement_list.html', {'listiq': listq})


def rand_advertisement_list(request, *args, **kwargs):
    listq = ['Мастер на час', 'Выведение из запоя', 'Услоги экскаватора погрузчика', "Услуги кошки"]
    random.shuffle(listq)
    return render(request, 'advertisement/advertisement_list.html', {'listiq': listq})


def homepage(request):
    urls = ['advertisement_one/', 'advertisement_two/', 'advertisement_three/', 'advertisement_four/',
            'advertisement_five/', 'regions/', 'about/', 'advertisements/','contacts/']
    block_content = ['Первое объявление', 'Второе объявление', 'Третье объявление', 'Четвертое объявление',
                     'Пятое объявление', 'Регионы', 'About', 'Домашняя работа','Контакты']
    data = {}
    for i in range(len(urls)):
        data[urls[i]] = block_content[i]
    return render(request, 'advertisement/homepage.html', context={'data': data})


def user_ip(request):
    ip = request.META.get('REMOTE_ADDR')
    return render(request, 'info/user_info.html', {'ip_adress': ip})


def base_adverisement(request):
    list_advertisements = ['Мастер на час',
                           "Выведение из запоя",
                           'Услуги экскаватора - погрузчика, гидромолота, ямобура']
    return render(request, 'advertisement/base_advertisement.html', {'advertisements': list_advertisements})


class About(TemplateView):
    template_name = 'advertisement/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Бесплатные объявления'
        context['title'] = 'Бесплатные объявления'
        context['description'] = 'Здесь вы моожете быстро и бесплатно продать или купить что-то, а также съесть смявла'
        context['menu'] = 'http://127.0.0.1:8000/'
        return context


class Regions(View):
    def get(self, request):
        # if request.method == 'GET':
        regions = ['Moscow', 'Obninsk', 'Riga']
        return render(request, 'info/regions.html', {'data': regions})

    def post(self, request):
        print('Region was successful created')
        return HttpResponse('Region was successful created')


class Counter(View):
    # template_name = 'advertisement/cbv.html'
    def __init__(self):
        self.counter = 0
    def __call__(self):
        #if request:
        self.counter += 1
        print(self.counter)

    def get(self, request):
        if request.method == 'GET':
            # print(self.counter)
            self.counter += 1
            data = {"header": 'В ПРОДАЖЕ', "list_adv": ['Продается Кошкино лукошко', 'Продаю свинью по профилю кабан',
                                                        'В ассортименте шило от кутюр', 'Продажа Петьки - забияки'],
                    'counter': self.counter}
            return render(request, 'advertisement/cbv.html', context=data)

    def post(self, request):
        if request.method == 'POST':
            self.counter += 1
            return HttpResponse('<a>Запись была сделана</a>')

class Templ(TemplateView):
    template_name = 'info/contacts.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['info'] = 'Информация'
        context['adress']='Улица Пушкина 17'
        context['phone_number'] = '875875875875'
        context['email'] = 'dogg@mail.ru'
        return context
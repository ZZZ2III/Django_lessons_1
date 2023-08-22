import datetime
from django.utils.translation import gettext as _
from django.views.decorators.cache import cache_page
from django.shortcuts import render
from time import sleep

# Create your views here.
def translation_example(request, *args, **kwargs):
    return render(request, 'translation_example.html')


def translation_homework(request, *args, **kwargs):
    return render(request, 'translation_homework.html')


def greetings_page(request, *args, **kwargs):
    greetings_message = _('Hello there! Today is %(date)s %(time)s') % {
        'date': datetime.datetime.now().date(),
        'time': datetime.datetime.now().time()
    }
    return render(request, 'greetings.html', context={'greetings_message': greetings_message})

#@cache_page(30)
def welcome(request, *args, **kwargs):
    sleep(4)
    return render(request, 'welcome.html')


def main_page(request, *args, **kwargs):
    return render(request, 'main.html')

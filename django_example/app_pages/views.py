from django.shortcuts import render


# Create your views here.
def translation_example(request, *args, **kwargs):
    return render(request, 'translation_example.html')


def translation_homework(request, *args, **kwargs):
    return render(request, 'translation_homework.html')

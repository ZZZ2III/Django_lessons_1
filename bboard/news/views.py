from django.shortcuts import render
from news.forms import NewsForm, CommentsForm
from django.views import View
from django.http import HttpResponseRedirect


# Create your views here.

class NewsFromView(View):
    def get(self, request):
        news_form = NewsForm()
        return render(request, 'news/makenew.html', context={'news_form': news_form})

    def post(self, request):
        news_form = NewsForm(request.POST)
        if news_form.is_valid():
            NewsForm.objects.create(**news_form.cleaned_data)
            return HttpResponseRedirect('/')

        return render(request, 'news/makenew.html', context={'news_form': news_form})


class CommetFormView(View):
    def get(self, request):
        comm_forms = CommentsForm()
        return render(request, 'news/makecomm.html', context={'comms_form': comm_forms})

    def post(self, request):
        comm_forms = CommentsForm(request.POST)
        if comm_forms.is_valid():
            CommentsForm.objects.create(**comm_forms.cleaned_data)
            raise HttpResponseRedirect('/')
        return render(request, 'news/makecomm.html', context={'comms_form': comm_forms})

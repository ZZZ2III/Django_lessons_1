from django.shortcuts import render
from news.forms import NewsForm, CommentsForm
from news.models import NewsModel,CommentsModel
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.

class NewsFromView(View):
    def get(self, request):
        news_form = NewsForm()
        return render(request, 'news/makenew.html', context={'news_form': news_form})

    def post(self, request):
        news_form = NewsForm(request.POST)
        if news_form.is_valid():
            NewsModel.objects.create(**news_form.cleaned_data)
            return HttpResponseRedirect('/')

        return render(request, 'news/makenew.html', context={'news_form': news_form})


class CommetFormView(View):
    def get(self, request):
        comm_forms = CommentsForm()
        return render(request, 'news/makecomm.html', context={'comms_form': comm_forms})

    def post(self, request):
        comm_forms = CommentsForm(request.POST)
        if comm_forms.is_valid():
            CommentsModel.objects.create(**comm_forms.cleaned_data)
            return HttpResponseRedirect('/')
        return render(request, 'news/makecomm.html', context={'comms_form': comm_forms})


class All_news(ListView):
    model = NewsModel
    template_name = 'news/all_news.html'
    context_object_name = 'news_list'
    # queryset = Advertisement.objects.all()[5:]


class SortedNews(DetailView):
    model = NewsModel
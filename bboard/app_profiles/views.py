from django.shortcuts import render
from app_profiles.forms import UserForm, AdvertisementForm
from django.views import View
from app_profiles.models import User, Advertisement
from django.http import HttpResponseRedirect


# Create your views here.

class UserFromView(View):
    def get(self, request):
        user_form = UserForm()
        return render(request, 'profiles/register.html', context={'user_from': user_form})

    def post(self, request):
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            User.objects.create(**user_form.cleaned_data)
            return HttpResponseRedirect('/')

        return render(request, 'profiles/register.html', context={'user_from': user_form})


class AdvertisementFormView(View):
    def get(self, request):
        adv_form = AdvertisementForm()
        return render(request, 'profiles/advertisement.html', context={'adv_form': adv_form})

    def post(self, request):
        adv_form = AdvertisementForm(request.POST)

        if adv_form.is_valid():
            Advertisement.objects.create(**adv_form.cleaned_data)
            return HttpResponseRedirect('/')

        return render(request, 'profiles/advertisement.html', context={'adv_form': adv_form})

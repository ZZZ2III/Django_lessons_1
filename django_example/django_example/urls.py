"""django_example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django_example.views import MainView
from django.conf import settings

urlpatterns = [
                  path('', MainView.as_view(), name='main'),
                  path('admin/', admin.site.urls),
                  path('users/', include('app_users.urls')),
                  path('employment/', include('app_employment.urls')),
                  path('files/', include('app_media.urls')),
                  path('goods/', include('app_goods.urls')),
                  path('app_logic/', include('app_logic.urls')),
                  path('app_pages/', include('app_pages.urls')),
                  path('i18n', include('django.conf.urls.i18n')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

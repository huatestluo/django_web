"""mainapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.conf.urls import url
from meal import views
from . import getdb

urlpatterns = [
    url(r'^$',views.demo),
    url(r'^huahua$',views.huahua),
    url(r'^index$',views.index),
    url(r'^add_db$',getdb.add_db),
    url(r'^select_db$',getdb.select_db),
    url(r'^select_all$',getdb.select_all),
    url(r'^meal_random$',views.meal_random),
]

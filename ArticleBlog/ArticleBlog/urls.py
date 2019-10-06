"""ArticleBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,re_path
from ArticleBlog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('li/',newlist),
    # path('l/',newlis),
    # path('l/index.html/',newl),
    # re_path('page/(?P<page>\d{1,2})',index)
    # path('luo/',form_exam),
    path('index/',index),
    # path('about/',about),
    # path('listpic/',listpic),
    # re_path(r'newslistpic/(?P<type>\w+)/(?P<p>\d{1,2})',newslistpic),
    # re_path(r'newslistpic/(?P<p>\d{1,2})',newslistpic),
    path('base/',register),
    # path('agp/', ajax_get_page),
    # path('agd/', ajax_get_data),
    # path('app/', ajax_post_page),
    # path('apd/', ajax_post_data),
    path('cookies/', cookies),
    path('logout/', logout),
]

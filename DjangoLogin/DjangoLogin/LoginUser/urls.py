from django.urls import path,re_path
from LoginUser.views import *
urlpatterns = [
    # path('register/', register),
    path('login/', login),
    # path('index/', index),
    # path('register/',register),

    # path('add_goods/', goods_update),
    # re_path('goods_list/(?P<page>\d+)/(?P<status>[01])/', goods_list),
    # path('base/', base),
    # re_path('qq/(?P<page>\d+)/(?P<status>[01])/', goods_list_api),
    # re_path('goods_status/(?P<state>\w+)/(?P<id>\d+)/', goods_status),
    # path('qq/',register),
    # path('qd/',qj)
]
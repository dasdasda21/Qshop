from django.urls import path,include,re_path
from Seller.views import *

urlpatterns = [
    path('register/', register),
    path('login/', login),
    path('index/', index),
    path('logout/', logout),
    path('goods_list/', goods_list),
    re_path('goods_list/(?P<page>\d+)/(?P<status>[01])/', goods_list),
    re_path('goods_status/(?P<state>\w+)/(?P<id>\d+)/', goods_status),
    path('personal_info/', personal_info),
    path('goods_add/',goods_add),
    path('slc/',send_login_code),
    re_path(r'order_list/(?P<status>\d{1})',order_list),
    path('change_order/',change_order)





]

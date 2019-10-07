# from django.shortcuts import render
# from Seller.models import *
# from Seller.views import setPassword
# from django.shortcuts import HttpResponseRedirect
# from Buyer.models import *
# def loginValid(fun):
#     def inner(request,*args,**kwargs):
#         cookie_user = request.COOKIES.get("username")
#         session_user = request.session.get("username")
#         if cookie_user and session_user and cookie_user == session_user:
#             return fun(request,*args,**kwargs)
#         else:
#             return HttpResponseRedirect("/Buyer/login/")
#     return inner
# def login(request):
#     if request.method =="POST":
#         password =request.POST.get("pwd")
#         email =request.POST.get("email")
#         user =LoginUser.objects.filter(email=email).first()
#         if user:
#             db_password =user.password
#             password =setPassword(password)
#             if db_password ==password:
#                 response =HttpResponseRedirect("/buyer/index")
#                 response.set_cookie("username",user.username)
#                 response.set_cookie("user_id",user.id)
#                 request.session["username"]=user.username
#                 return response
#     return render(request,"buyer/login.html")
# def register(request):
#     error=""
#     if request.method =="POST":
#         username=request.POST.get("username")
#         password =request.POST.get("pwd")
#         email =request.POST.get("email")
#         user = LoginUser()
#         if username:
#            db_email =user.email
#            if email!=db_email:
#              user.username = username
#              user.password=setPassword(password)
#              user.email =email
#              user.save()
#              return HttpResponseRedirect("/buyer/login/")
#            else:
#                error="邮箱已被注册"
#         else:
#             error="用户名已被注册"
#     else:
#         return render(request,"buyer/register.html")
# def index(request):
#     goods_type =GoodsType.objects.all() #获取到所有类型
#     result= []
#     for ty in goods_type:       #遍历出每种类型
#         goods =ty.goods_set.order_by("-goods_pro_time")
#         #每种类型根据出产日期排序后的goods ,外键调用
#         if len(goods) >=1:  #某种类型的商品种类大于4
#             goods =goods[:4]    #取前4
#             result.append({"type":ty,"goods_list":goods})
#     return render(request,"buyer/index.html",locals())
#
# def goods_list(request):
#     """
#     type 代表请求的类型
#         t 按照类型查询
#             keywords必须是类型id
#         k 按照关键字查询
#             keywords可以是任何东西
#     keywords 代表请求的关键字
#     """
#     request_type = request.GET.get("type") #获取请求的类型 t 类型查询 k关键字查询
#     keyword = request.GET.get("keywords") #查询的内容 t类型 k为类型id  k类型 k为关键字
#     goods_list = [] #返回的结果
#     if request_type == "t": #t类型查询
#         if keyword:
#             id = int(keyword)
#             goods_type = GoodsType.objects.get(id = id) #先查询类型
#             goods_list = goods_type.goods_set.order_by("-goods_pro_time") #再查询类型对应的商品
#     elif request_type == "k":
#         if keyword:
#             goods_list = Goods.objects.filter(goods_name__contains=keyword).order_by("-goods_pro_time") #模糊查询商品名称含有关键字的商品
#     if goods_list: #限定推荐的条数
#         lenth = len(goods_list) / 5
#         if lenth != int(lenth):
#             lenth += 1
#         lenth = int(lenth)
#         recommend = goods_list[:lenth]
#     return render(request,"buyer/goods_list.html",locals())
#
# def goods_detail(request,id):
#     goods = Goods.objects.get(id = int(id))
#     return render(request,"buyer/detail.html",locals())
#
#
# def user_center_info(request):
#     return render(request,"buyer/user_center_info.html",locals())
# import datetime
# import time
# def place_order(request):
#     goods_id =request.GET.get("goods_id")
#     count =request.GET.get("count")
#     if goods_id and count:
#         order =PayOrder()
#         order.order_number =str(time.time()).replace(".","")
#         order.order_data=datetime.datetime.now()
#         order.order_status=0
#
#         order.order_user= LoginUser.objects.get(id=int(request.COOKIES.get("user_id")))
#         order.save()
#         goods = Goods.objects.get(id = int(goods_id))
#         order_info = OrderInfo()
#         order_info.order_id = order
#         order_info.goods_id = goods.id
#         order_info.goods_picture = goods.picture
#         order_info.goods_name = goods.goods_name
#         order_info.goods_count = int(count)
#         order_info.goods_price = goods.goods_price
#         order_info.goods_total_price = goods.goods_price*int(count)
#         order_info.store_id = goods.goods_store #商品卖家，goods.goods_store本身就是一条卖家数据
#         order_info.save()
#         order.order_total = order_info.goods_total_price
#         order.save()
#     return render(request,"buyer/place_order.html",locals())
# from alipay import AliPay
# from Qshop.settings import alipay_public_key_string,alipay_private_key_string
# def AlipayViews(request):
#     order_number =request.GET.get("order_number")
#     order_total =request.GET.get("total")
#     alipay = AliPay(
#         appid="2016101200667739",
#         app_notify_url=None,
#         app_private_key_string=alipay_private_key_string,
#         alipay_public_key_string=alipay_public_key_string,
#         sign_type="RSA2"
#     )
#     order_string = alipay.api_alipay_trade_page_pay(
#         out_trade_no=order_number,
#         total_amount=str(order_total),
#         subject="生鲜交易",
#         return_url="http://127.0.0.1:8000/buyer/pay_result/",
#         notify_url="http://127.0.0.1:8000/buyer/pay_result/",
#     )
#     result ="https://openapi.alipaydev.com/gateway.do?"+order_string
#     return HttpResponseRedirect(result)
#
# def pay_result(request):
#     out_trade_no =request.GET.get("out_trade_no")
#     if out_trade_no:
#         order =PayOrder.objects.get(order_number=out_trade_no)
#         order.order_status=1
#         order.save()
#     return render(request,"buyer/place_order.html",locals())
#
# def logout(request):
#     url = request.META.get("HTTP_REFERER", "/Buyer/index/")
#     response = HttpResponseRedirect(url)
#     for k in request.COOKIES:
#         response.delete_cookie(k)
#     del request.session["username"]
#     return response


# Create your views here.


from Seller.models import *
from django.shortcuts import render,HttpResponseRedirect
from django.http import JsonResponse

import hashlib
def setPassword(password):
    md5 =hashlib.md5()
    md5.update(password.encode())
    result =md5.hexdigest()
    return result

def register(request):
    error=[]
    if request.method=="POST":
        username =request.POST.get("user_name")
        password =request.POST.get("pwd")
        email =request.POST.get("email")
        user =LoginUser()
        if email:
            db_email =LoginUser.objects.filter(email=email).first()
            db_username =LoginUser.objects.filter(username=username).first()
            if not db_email:
                if not db_username:
                    user.password =setPassword(password)
                    user.username =username
                    user.email =email
                    user.save()
                    error = "注册成功"
                else:
                    error ="用户名已存在"
            else:
                error ="邮箱已被注册"
        else:
            error ="邮箱不可以为空"
    return render(request,"buyer/register.html",locals())

def login(request):
    error=[]
    if request.method=="POST":              #校验功能
        password =request.POST.get("pwd")
        email =request.POST.get("email")
        if email:
            db_email =LoginUser.objects.filter(email=email).first()
            if db_email:
                db_password =db_email.password
                password =setPassword(password)
                if db_password==password:
                    response =HttpResponseRedirect("/buyer/index/")
                    response.set_cookie("username",db_email.username)
                    response.set_cookie("user_id",db_email.id)
                    request.session["username"]=db_email.username
                    return response
                else:
                    error ="密码错误"
            else:
                error="请输入正确的邮箱"
        else:
            error="邮箱不可以为空"
    return render(request,"buyer/login.html",locals())
def index(request):
    result=[]
    goods_type =GoodsType.objects.all()
    for ty in goods_type:
        goods =ty.goods_set.order_by("-goods_pro_time")
        if len(goods) >=1:
            goods =goods[:4]
            result.append({"type":ty,"goods_list":goods})
    return render(request,'buyer/index.html',locals())
def goods_list(request):
    request_type =request.GET.get("type")
    keyword =request.GET.get("keywords")
    goods_list=[]
    if request_type == "t":
        if keyword:
            id=int(keyword)
            goods_type =GoodsType.objects.get(id=id)
            goods_list=goods_type.goods_set.order_by("-goods_pro_time")
    elif request_type =="k":
        if keyword:
            goods_list =Goods.objects.filter(goods_name__contains=keyword).order_by("-goods_pro_time")
    if goods_list:
        lenth =len(goods_list)/5
        if lenth != int(lenth):
            lenth+=1
        lenth = int(lenth)
        recommend =goods_list[:lenth]
    return render(request, "buyer/goods_list.html", locals())

def detail(request,id):
    goods =Goods.objects.get(id=int(id))
    return render(request,"buyer/detail.html",locals())
from Buyer.models import *
import time
import datetime
def pay_order(request):
    goods_id =request.GET.get("goods_id")
    count =request.GET.get("count")
    if goods_id and count:
        order =PayOrder()
        order.order_number = str(time.time()).replace(".","")
        order.order_data =datetime.datetime.now()
        order.order_status=0
        order.order_user=LoginUser.objects.get(id=int(request.COOKIES.get("user_id")))
        order.save()

        goods =Goods.objects.get(id=int(goods_id))
        order_info =OrderInfo()
        order_info.order_id =order
        order_info.goods_id=goods_id
        order_info.goods_picture = goods.picture
        order_info.goods_name = goods.goods_name
        order_info.goods_count = int(count)
        order_info.goods_price = goods.goods_price
        order_info.goods_total_price = goods.goods_price * int(count)
        order_info.store_id = goods.goods_store  # 商品卖家，goods.goods_store本身就是一条卖家数据
        order_info.save()
        order.order_total = order_info.goods_total_price
        order.save()
    return render(request, "buyer/pay_order.html", locals())

def pay_order_more(request):
    data = request.GET
    data_item = data.items()
    request_data = []
    for key,value in data_item:
        if key.startswith("check_"):
            goods_id = key.split("_",1)[1]
            count = data.get("count_"+goods_id)
            request_data.append((int(goods_id),int(count)))
    if request_data:
        #保存订单表，但是保存总价
        order = PayOrder()
        order.order_number = str(time.time()).replace(".","")
        order.order_data = datetime.datetime.now()
        order.order_status = 0
        order.order_user = LoginUser.objects.get(id = int(request.COOKIES.get("user_id"))) #订单对应的买家
        order.save()
        #保存订单详情
        #查询商品的信息
        order_total = 0
        for goods_id,count in request_data:
            goods = Goods.objects.get(id = int(goods_id))
            order_info = OrderInfo()
            order_info.order_id = order
            order_info.goods_id = goods.id
            order_info.goods_picture = goods.picture
            order_info.goods_name = goods.goods_name
            order_info.goods_count = int(count)
            order_info.goods_price = goods.goods_price
            order_info.goods_total_price = goods.goods_price*int(count)
            order_info.store_id = goods.goods_store #商品卖家，goods.goods_store本身就是一条卖家数据
            order_info.save()
            order_total += order_info.goods_total_price #总价计算
        order.order_total = order_total
        order.save()
    return render(request,"buyer/pay_order.html",locals())

from Qshop.settings import alipay_public_key_string,alipay_private_key_string
from alipay import AliPay
from Qshop.settings import alipay_public_key_string,alipay_private_key_string
def AlipayViews(request):
    order_number =request.GET.get("order_number")    #支付功能
    order_total =request.GET.get("total")
    alipay = AliPay(
        appid="2016101200667739",
        app_notify_url=None,
        app_private_key_string=alipay_private_key_string,
        alipay_public_key_string=alipay_public_key_string,
        sign_type="RSA2"
    )
    order_string = alipay.api_alipay_trade_page_pay(
        out_trade_no=order_number,
        total_amount=str(order_total),
        subject="生鲜交易",
        return_url="http://127.0.0.1:8000/buyer/pay_result/",
        notify_url="http://127.0.0.1:8000/buyer/pay_result/",
    )
    result ="https://openapi.alipaydev.com/gateway.do?"+order_string
    return HttpResponseRedirect(result)


def add_cart(request):                #前端ajax通过路由传递参数goods_id 和count
    result ={                           #此视图为点击加入购物车的方法
        "code":200,
        "data":""
    }
    if request.method=="POST":
        id =int(request.POST.get("goods_id"))
        count =int(request.POST.get("count",1))
        goods =Goods.objects.get(id=id)
        cart=Cart()
        cart.goods_name=goods.goods_name
        cart.goods_number=count
        cart.goods_price=goods.goods_price
        cart.goods_picture=goods.picture
        cart.goods_id=id
        cart.goods_total=goods.goods_price*count
        cart.cart_user=request.COOKIES.get("user_id")
        cart.save()
        result["data"] ="jiaruchenggong"
    else:
        result["code"]=500
        result["data"]="qing qiu fang shi cuo wu"
    return JsonResponse(result)

def cart(request):                         #购物车视图需要
    user_id = request.COOKIES.get("user_id")
    goods =Cart.objects.filter(cart_user=int(user_id)).order_by("-id")
    count =goods.count()
    return render(request,"buyer/cart.html",locals())

def user_center_order(request):
    user_id = request.COOKIES.get("user_id")
    user = LoginUser.objects.get(id = int(user_id))
    order_list = user.payorder_set.order_by("-order_data")
    return render(request,"buyer/user_center_order.html", locals())

from CeleryTask.tasks import add
def get_task(request):
    num1 = request.GET.get("num1",1)
    num2 = request.GET.get("num2",2)
    add.delay(int(num1),int(num2))
    return JsonResponse({"data":"success"})

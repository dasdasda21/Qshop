import hashlib
from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.core.paginator import Paginator
from django.http import JsonResponse
from Seller.models import *

def loginValid(fun):
    def inner(request,*args,**kwargs):
        cookie_name =request.COOKIES.get("username")
        session_name =request.session.get("username")
        if cookie_name and session_name and cookie_name==session_name:
            return fun(request,*args,**kwargs)
        else:
            return HttpResponseRedirect("/seller/login/")
    return inner
def setPassword(password):
    md5 =hashlib.md5()
    md5.update(password.encode())
    result =md5.hexdigest()
    return result

def register(request):
    error_message =""
    if request.method =="POST":
        email =request.POST.get("email")
        password = request.POST.get("password")
        if email:
            user =LoginUser.objects.filter(email=email).first()
            if not user:
                new_user =LoginUser()
                new_user.email=email
                new_user.password=setPassword(password)
                new_user.username=email
                new_user.save()
            else:
                error_message="邮箱已被注册"
        else:
            error_message="邮箱不可以为空"
    return render(request,"seller/register.html",locals())
import time,datetime
from django.views.decorators.cache import cache_page
@cache_page(60*15)
def login(request):
    error_message=""
    if request.method=="POST":
        email =request.POST.get("email")
        password =request.POST.get("password")
        code = request.POST.get("valid_code")
        if email:
            user =LoginUser.objects.filter(email=email).first()
            if user:
                db_password =user.password
                password =setPassword(password)
                if db_password ==password:
                    codes = Valid_Code.objects.filter(code_user=email).order_by("-code_time").first()
                    # 校验验证码是否存在，是否过期，是否被使用
                    now = time.mktime(datetime.datetime.now().timetuple())
                    db_time = time.mktime(codes.code_time.timetuple())
                    t = (now - db_time) / 60
                    if codes and codes.code_state == 0 and t <= 5 and codes.code_content.upper() ==code.upper():
                        response =HttpResponseRedirect("/seller/index/")
                        response.set_cookie("username",user.username)
                        response.set_cookie("user_id",user.id)
                        request.session["username"] =user.username
                        print(response.cookies)
                        return response
                    else:
                        error_message="验证码错误"
                else:
                    error_message="密码错误"
            else:
                error_message="用户名不存在"
        else:
            error_message="邮箱不可以为空"
    return render(request,"seller/login.html",locals())

def logout(request):
    response =HttpResponseRedirect("/login/")
    keys =request.COOKIES.keys()
    for k in keys:
        response.delete_cookie(k)
    del request.session["username"]
    return response

@loginValid
def index(request):
    return render(request,"seller/index.html",locals())

@loginValid
def goods_list(request,status,page=1):
    user_id =request.COOKIES.get("user_id")
    user =LoginUser.objects.get(id=int(user_id))
    if status=="1":
        goodses =Goods.objects.filter(goods_store=user,goods_status=1)
    elif status =="0":
        goodses =Goods.objects.filter(goods_store=user,goods_status=0)
    else:
        goodses =Goods.objects.all()
    all_goods =Paginator(goodses,10)            # django 分页功能
    goods_list =all_goods.page(page)
    return render(request,"seller/goods_list.html",locals())

@loginValid
def goods_status(request,state,id):
    id = int(id)
    goods = Goods.objects.get(id = id)
    if state == "up":
        goods.goods_status = 1
    elif state == "down":
        goods.goods_status = 0
    goods.save()
    url = request.META.get("HTTP_REFERER","/goods_list/1/1")
    return HttpResponseRedirect(url)

@loginValid
def personal_info(request):
    user_id = request.COOKIES.get("user_id")
    user = LoginUser.objects.get(id = int(user_id))
    if request.method == "POST":
        user.username = request.POST.get("username")
        user.gender = request.POST.get("gender")
        user.age = request.POST.get("age")
        user.phone_number = request.POST.get("phone_number")
        user.address = request.POST.get("address")
        user.photo = request.FILES.get("photo")
        user.save()
    return render(request,"seller/personal_info.html",locals())


@loginValid
def goods_add(request):
    goods_type_list = GoodsType.objects.all()
    if request.method == "POST":
        data = request.POST
        files = request.FILES

        goods = Goods()
        #常规保存
        goods.goods_number = data.get("goods_number")
        goods.goods_name = data.get("goods_name")
        goods.goods_price = data.get("goods_price")
        goods.goods_count = data.get("goods_count")
        goods.goods_location = data.get("goods_location")
        goods.goods_safe_date = data.get("goods_safe_date")
        goods.goods_pro_time = data.get("goods_pro_time") #出厂日期格式必须是yyyy-mm-dd格式
        goods.goods_status = 1

        #保存外键类型
        goods_type_id = int(data.get("goods_type"))
        goods.goods_type = GoodsType.objects.get(id = goods_type_id)
        #保存图片
        picture = files.get("picture")
        goods.picture = picture
        #保存对应的卖家
        user_id = request.COOKIES.get("user_id")
        goods.goods_store = LoginUser.objects.get(id = int(user_id))

        goods.save()

    return render(request,"seller/goods_add.html",locals())


# import json
# import requests
# from Qshop.settings import DING_URL
# from  django.views.decorators.csrf import csrf_exempt
# def sendDing(content,to=None):
#     headers = {
#         "Content-Type": "application/json",
#         "Charset": "utf-8"
#     }
#     requests_data = {
#         "msgtype": "text",
#         "text": {
#             "content": content
#         },
#         "at": {
#             "atMobiles": [
#             ],
#             "isAtAll": True
#         }
#     }
#     if to:
#         requests_data["at"]["atMobiles"].append(to)
#         requests_data["at"]["isAtAll"] = False
#     else:
#         requests_data["at"]["atMobiles"].clear()
#         requests_data["at"]["isAtAll"] = True
#     sendData = json.dumps(requests_data)
#     response = requests.post(url=DING_URL, headers=headers, data=sendData)
#     content = response.json()
#     return content
#
# import random
# def random_code(len=6):
#     """
#     生成6位验证码
#     """
#     string = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     valid_code = "".join([random.choice(string) for i in range(len)])
#     return valid_code
#
# @csrf_exempt
# def send_login_code(request):
#     result = {
#         "code": 200,
#         "data": ""
#     }
#     if request.method == "POST":
#         email = request.POST.get("email")
#         code = random_code()
#         c = Valid_Code()
#         c.code_user = email
#         c.code_content = code
#         c.save()
#         send_data = "%s的验证码是%s,打死也不要告诉别人哟"%(email,code)
#         sendDing(send_data) #发送验证
#         result["data"] = "发送成功"
#     else:
#         result["code"] = 400
#         result["data"] = "请求错误"
#     return JsonResponse(result)

import json
import requests
from Qshop.settings import DING_URL
def sendDing(content,to=None):
    headers = {
        "Content-Type":"application/json",
        "Charset":"utf-8"
    }
    requests_data ={
        "msgtype":"text",
        "text":{
            "content": content
        },
        "at":{
            "atMobiles":[
            ],
            "isAtAll":True
        }
    }
    if to:
        requests_data["at"]["atMobiles"].append(to)
        requests_data["at"]["isAtAll"]=False
    else:
        requests_data["at"]["atMobiles"].clear()
        requests_data["at"]["isAtAll"] = True


    sendData = json.dumps(requests_data)
    response = requests.post(url = DING_URL,headers=headers,data=sendData)
    content = response.json()
    return content
import random
def random_code(len=6):
    string = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    value_code = "".join([random.choice(string) for i in range(len)])
    return value_code

def send_login_code(request):
    result = {
        "code":200,
        "data":""
    }
    if request.method=="POST":
        email=request.POST.get("email")
        code = random_code()
        c = Valid_Code()
        c.code_user=email
        c.code_content =code
        c.save()
        send_data ="%s的验证码是%s"%(email,code)
        sendDing(send_data)
        result["data"] = "发送成功"
    else:
        result["code"]=400
        result["data"]="请求错误"
    return JsonResponse(result)

from Buyer.models import *
def order_list(request,status):
    status = int(status)
    # store_order = OrderInfo.objects.filter(order_status=status).order_by("-id")
    user_id = request.COOKIES.get("user_id")
    store = LoginUser.objects.get(id = user_id)
    store_order = store.orderinfo_set.filter(order_status=status).order_by("-id")
    return render(request,"seller/code_list.html",locals())

def change_order(request):
    order_id = request.GET.get("order_id")
    order_status =request.GET.get("order_status")
    order = OrderInfo.objects.get(id=order_id)
    order.order_status = int(order_status)
    order.save()
    return JsonResponse({"data":"修改成功"})



# Create your views here.

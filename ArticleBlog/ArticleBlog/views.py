from django.shortcuts import render_to_response
from django.core.paginator import Paginator
from Article.models import *
from django.shortcuts import render
from Article.forms import Register
from django.http import JsonResponse
def register(request):
    register_form=Register()
    if request.method=="POST": #判断请求方式
        data_valid = Register(request.POST)
        if data_valid.is_valid():
            clean_data =data_valid.cleaned_data
            username = clean_data.get("username")
            password = clean_data.get("password")
            email =clean_data.get("email")
            u=User()
            u.username = username  # 保存用户名
            u.password = setPassword(password)  # 保存密码
            u.email = email
            u.save()  # 保存数据
        else:
            errors = data_valid.errors
            print(errors)
    return render(request, "register.html", locals())
def user_valid(request):
    email = request.GET.get("email") #获取请求的email
    result = {"code":"400","data":""} #定义返回的数据格式
    if email:
        user = User.objects.filter(email = email).first() #安装email查询用户
        if user: #用户存在，邮箱不可用
            result["data"] = "当前邮箱已经完成注册，请登录"
        else: #用户不存在，邮箱可以用
            result["code"] = "200"
            result["data"] = "当前邮箱可以注册"
    else: #空
        result["data"] = "邮箱不可以为空"
    return JsonResponse(result)


import hashlib
def setPassword(password):
    md5 =hashlib.md5()
    md5.update(password.encode())
    result= md5.hexdigest()
    return result
from django.http import HttpResponseRedirect
def loginValid(fun):
    def inner(request,*args,**kwargs):
        username = request.COOKIES.get("username")
        session_username=request.session.get("username")
        if username:
            return fun(request,*args,**kwargs)
        else:
            return HttpResponseRedirect("/cookies/")
    return inner
def cookies(request):
    if request.method=="POST":
        username =request.POST.get("username")
        password =request.POST.get("password")
        user = User.objects.filter(username = username).first()
        if user:
            db_password = user.password
            password = setPassword(password)
            if password == db_password:
                response =HttpResponseRedirect("/index/")
                response.set_cookie("username", "user.username")
                response.set_cookie("age", "18")
                request.session["username"]=user.username
                return response  # 这里写路由不写页面
    return render(request, "cookies.html")
@loginValid
def index(request):
    new_article =Article.objects.order_by("-public_time")[:6]
    recom_article = Article.objects.filter(recommend=1).order_by("-public_time")[:7]
    click_article =Article.objects.order_by("-click")[:12]
    return render_to_response("index.html",locals())

def logout(request):
    response = HttpResponseRedirect("/cookies/")
    response.delete_cookie("username")
    response.delete_cookie("age")
    return response












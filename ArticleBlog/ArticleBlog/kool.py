from django.http import HttpResponse
from django.template.loader import get_template
# def index(request,name,age):
#     template = get_template("easay.html")
#     result = template.render({"name":name, "age":age})
#     return HttpResponse(result)
class Saying:
    def say(self):
        return "hahaha"
def chen(request):
    data ={
        "name":"laowang",
        "age":19,
        "project":["php","python","java","c","c++"],
        "score":{"python":100,"php":120},
        "s":Saying()
    }
    ok = get_template("easay.html")
    result = ok.render(data)
    return HttpResponse(result)
def nice(request):
    data = {
        "hapi":[
            {"name":"cf","dengji":"21"},
            {"name":"lualu","dengji":"12"},
            {"name":"dnf","dengji":"31"},
            {"name":"feiche","dengji":"23"},

        ],
        "outer":"3123",
        "login_valid":0,
        "commit":"<script>alert('hello world')</script>"
    }
    tem = get_template('easay.html')
    result = tem.render(data)
    return HttpResponse(result)
articles = [
    {"id": 1, "title": "背影", "author": "朱自清", "public_time": "1883-3-3","content": "买橘子的故事","image":"image/by.jpg"},
    {"id": 2, "title": "骆驼祥子", "author": "老舍", "public_time": "1885-3-3", "content": "北京最早的D哥的爱情故事","image":"image/ltxz.jpg"},
    {"id": 3, "title": "鬼吹灯", "author": "三叔", "public_time": "1873-3-3", "content": "空气对流的故事","image":"image/gcd.jpg"},
    {"id": 4, "title": "蜀道难", "author": "李白", "public_time": "1643-3-3", "content": "那是一条神奇的天路","image":"image/adn.jpg"},
    {"id": 5, "title": "道德经", "author": "老子", "public_time": "1873-3-3", "content": "教育的故事","image":"image/ddj.jpg"}
]
def easy(request):
    tem = get_template("index.html")
    result = tem.render({"articles":articles})
    return HttpResponse(result)
def page(request,id):
    id = int(id)
    article = ""
    for art in articles:
        if art["id"] == id:
            article = art
            break
    template = get_template("page.html")
    result = template.render({"article":article})
    return HttpResponse(result)
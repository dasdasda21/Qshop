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


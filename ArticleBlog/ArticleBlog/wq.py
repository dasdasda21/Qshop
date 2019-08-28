from django.http import HttpResponse
from django.template.loader import get_template
def che(request):
    template = get_template("base.html")
    result = template.render({})
    return HttpResponse(result)
def c(request):
    template = get_template("about.html")
    result = template.render({})
    return HttpResponse(result)
def d(request):
    template = get_template("index.html")
    result = template.render({})
    return HttpResponse(result)
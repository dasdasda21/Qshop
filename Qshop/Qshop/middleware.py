from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse
class MiddleWareTest(MiddlewareMixin):
    def process_request(self,request):
        request_ip = request.META["REMOTE_ADDR"]
        if request_ip == "10.10.14.89":
            return HttpResponse("非法ip")


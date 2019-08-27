# from django.http import HttpResponse
# from django.template.loader import get_template#这里用来加载settings的templates配置当中的html页面
# def index(request):
#     template = get_template("index.html")
#     result = template.render({"name":"老李"})
#     return HttpResponse(result)
# # def page_list(request,page):
# #     page=int(page)#page来自于url
# #     template = get_template("page_list.html")#加载页面
# #     result = template.render({"page":page})#类似字符串的渲染%s %a，将url传进来的page渲染到页面
# #     return HttpResponse(result)#返回的内容是需要渲染的结果
#
#
# class Saying:
#     def say(self):
#         return "hahaha"
# def template_variable(request):
#     data = {
#         "name":"chen",
#         "an_name":"luo",
#         "age":15,
#         "project":["php","linux","java","python","c","c++","易"],
#         "score":{"python":100,"php":120},
#         "s":Saying()
#
#     }
#     tem = get_template("template_variable.html")
#     result = tem.render(data)
#     return HttpResponse(result)
#
# def template_label(request):
#     data ={
#         "teacher": [
#             {"name": "老边", "age": 18},
#             {"name": "老张", "age": 23},
#             {"name": "老温", "age": 43},
#             {"name": "老王", "age": 65},
#             {"name": "老申", "age": 48}
#         ],
#         "outer": "abc",
#         "login_valid": 0,
#         "commit": "<script>alert('hello world')</script>"
#
#
#     }
#     tem = get_template('template_label.html')
#     result = tem.render(data)
#     return HttpResponse(result)
# articles = [
#     {"id": 1, "title": "背影", "author": "朱自清", "public_time": "1883-3-3", "content": "买橘子的故事"},
#     {"id": 2, "title": "骆驼祥子", "author": "老舍", "public_time": "1885-3-3", "content": "北京最早的D哥的爱情故事"},
#     {"id": 3, "title": "鬼吹灯", "author": "三叔", "public_time": "1873-3-3", "content": "空气对流的故事"},
#     {"id": 4, "title": "蜀道难", "author": "李白", "public_time": "1643-3-3", "content": "那是一条神奇的天路"},
#     {"id": 5, "title": "道德经", "author": "老子", "public_time": "1873-3-3", "content": "教育的故事"}
# ]
# def page_list(request):
#     template=get_template("page_list.html")
#     result = template.render({"articles":articles})
#     return HttpResponse(result)
# def page(request,id):
#     id=int(id)
#     article=""
#     for art in articles:
#         if art["id"]==id:
#             article =art
#             break
#     template=get_template("page.html")
#     result = template.render({"article":articles})
#     return HttpResponse(result)
# from django.http import HttpResponse
# from

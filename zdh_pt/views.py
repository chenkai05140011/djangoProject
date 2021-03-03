from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import time
# Create your views here.

#个人信息
def grxx(requset):
    context = {
        "name": "上海悠悠",
        "n_name": "chenkai",
        "age": "27",
        "fancy": ["python", "selenium", "jenkins"],
        "blog": {
            "url": "https://baidu.com",
            "img": "/static/1.jpg"
        }
    }

    class Myblog():
        def __init__(self):
            self.guanzhu = 1000
            self.fensi =10
        def guanzhu(self):
            return self.guanzhu
        def fensi(self):
            return self.fensi
    my_blog = Myblog()
    context["myblog"] = my_blog
    print(context)
    return render(requset, "grxx.html", context=context)



def hello(requset):
    #return HttpResponse("hello word")
    result = {
        "code": 0,
        "msg": "success",
        "data": []
    }
    return JsonResponse(result)
year = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
def login(requsrt):
    if requsrt.method == "GET":
        return render(requsrt, "login.html", {"year": year})
    else:
        result = {
            "code": 0,
            "msg": "success",
            "data": []
        }
        return JsonResponse(result)



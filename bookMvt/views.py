from django.shortcuts import render

# Create your views here.


def Test(request):
    return render(request,"bookapp/index.html")

# 用于extends 集成模板的学习
def showIndex(request):
    return render(request,"bookmvt/index.html")
def showUser1(request):
    return render(request,"bookmvt/user1.html")
def showUser2(request):
    return render(request,"bookmvt/user2.html")

# 用于html的转义

def htmlChangeTest(request):
    content = {
        "t1":"<h1>htmlChangeTest</h1>",
        "t2":"<h1>htmlChangeTest123</h1>"
    }
    return render(request,"bookmvt/htmlChangeTest.html",content)



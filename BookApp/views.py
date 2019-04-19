from django.shortcuts import render, redirect
from django.db.models import Max, F, Q
from django.http import *
# Create your views here.
from .models import *


def show(request):
    bookInfo = BookInfo.bookManager.all()
    maxBookInfo = BookInfo.bookManager.aggregate(Max("bpub_date"))
    maxGt100BookInfo = BookInfo.bookManager.filter(breadnum__gt=100)  # 查询月大量大于100的
    maxGtBookInfo1 = BookInfo.bookManager.filter(breadnum__gt=F("bcomment") * 5)  # 查询月大量大于评论书的
    maxGtBookInfo2 = BookInfo.bookManager.filter(breadnum__gt=100, btitle__contains='贝')  # 查询月大量大于评论书的
    maxGtBookInfo2 = BookInfo.bookManager.filter(breadnum__gt=100).filter(btitle__contains='贝')
    maxGtBookInfo3 = BookInfo.bookManager.filter(Q(btitle__contains='贝') | Q(isDelete=0))  # 查询名字包含贝切isDelete=0的数据信息
    print("*" * 15)
    print(maxBookInfo)
    print(bookInfo)
    print(maxGtBookInfo1)

    content = {
        "title": "卡卡罗特",
        'bookList': bookInfo,
        'maxBookInfo': maxBookInfo,
        'maxGt100BookInfo': maxBookInfo,
        'maxGtBookInfo1': maxGtBookInfo1,
        'maxGtBookInfo2': maxGtBookInfo2,
        'maxGtBookInfo3': maxGtBookInfo3,
    }

    return render(request, 'bookapp/index.html', content)


def index(request, p1, p2, p3):
    bookInfo = BookInfo.bookManager.all()
    maxBookInfo = BookInfo.bookManager.aggregate(Max("bpub_date"))
    maxGt100BookInfo = BookInfo.bookManager.filter(breadnum__gt=100)  # 查询月大量大于100的
    maxGtBookInfo1 = BookInfo.bookManager.filter(breadnum__gt=F("bcomment") * 5)  # 查询月大量大于评论书的
    maxGtBookInfo2 = BookInfo.bookManager.filter(breadnum__gt=100, btitle__contains='贝')  # 查询月大量大于评论书的
    maxGtBookInfo2 = BookInfo.bookManager.filter(breadnum__gt=100).filter(btitle__contains='贝')
    maxGtBookInfo3 = BookInfo.bookManager.filter(Q(btitle__contains='贝') | Q(isDelete=0))  # 查询名字包含贝切isDelete=0的数据信息
    print("*" * 15)
    print(maxBookInfo)
    print(bookInfo)
    print(maxGtBookInfo1)

    content = {
        "title": "卡卡罗特",
        'bookList': bookInfo,
        'maxBookInfo': maxBookInfo,
        'maxGt100BookInfo': maxBookInfo,
        'maxGtBookInfo1': maxGtBookInfo1,
        'maxGtBookInfo2': maxGtBookInfo2,
        'maxGtBookInfo3': maxGtBookInfo3,
        'p': p1,
    }

    return render(request, 'bookapp/index.html', content)


def details(request, p1, p2, p3):
    bookInfo = BookInfo.bookManager.all()
    maxBookInfo = BookInfo.bookManager.aggregate(Max("bpub_date"))
    maxGt100BookInfo = BookInfo.bookManager.filter(breadnum__gt=100)  # 查询月大量大于100的
    maxGtBookInfo1 = BookInfo.bookManager.filter(breadnum__gt=F("bcomment") * 5)  # 查询月大量大于评论书的
    maxGtBookInfo2 = BookInfo.bookManager.filter(breadnum__gt=100, btitle__contains='贝')  # 查询月大量大于评论书的
    maxGtBookInfo2 = BookInfo.bookManager.filter(breadnum__gt=100).filter(btitle__contains='贝')
    maxGtBookInfo3 = BookInfo.bookManager.filter(Q(btitle__contains='贝') | Q(isDelete=0))  # 查询名字包含贝切isDelete=0的数据信息
    print("*" * 15)
    print(maxBookInfo)
    print(bookInfo)
    print(maxGtBookInfo1)

    content = {
        "title": "卡卡罗特",
        'bookList': bookInfo,
        'maxBookInfo': maxBookInfo,
        'maxGt100BookInfo': maxBookInfo,
        'maxGtBookInfo1': maxGtBookInfo1,
        'maxGtBookInfo2': maxGtBookInfo2,
        'maxGtBookInfo3': maxGtBookInfo3,
        'p': p1,
        'time': "%s年-%s月-%s日" % (p1, p2, p3)
    }

    return render(request, 'bookapp/index.html', content)


def error(request):
    content = {

    }
    return render(request, '404.html', content)


def getTest(request):
    content = {

    }
    return render(request, 'bookapp/Test测试_request.html', content)


#  接收 一键对一值的问题
def getTest1(request):
    content = {
        "a1": request.GET['a'],
        "b1": request.GET['b'],
        "c1": request.GET['c'],
    }
    return render(request, 'bookapp/getTest1.html', content)


#  接收 一键多个值的问题
def getTest2(request):
    # 类似字典对象，
    a = request.GET.getlist("a")
    print(a)
    content = {
        "a1": a,
        "b1": request.GET['b'],
        "c1": request.GET['c'],
    }
    return render(request, 'bookapp/getTest2.html', content)


def postTest1(request):
    content = {}
    return render(request, "bookapp/postTest1.html", content)


def postTest2(request):
    uname = request.POST['uname']
    upwd = request.POST['upwd']
    ugerder = request.POST['ugerder']
    uhobby = request.POST.getlist('uhobby')
    content = {
        "uname": uname,
        "upwd": upwd,
        "ugerder": ugerder,
        "uhobby": uhobby,
        "title": "测试结果"
    }
    return render(request, "bookapp/postTest2.html", content)


def cookTest11(request):
    cookes = request.COOKIES
    response = HttpResponse()
    if "t1" in cookes:
        response.write(cookes["t1"])

    # response.set_cookie("t1","abc")
    return response


def cookTest1(request):
    # cookes = request.COOKIES
    # response = HttpResponse()
    # if "t1" in cookes:
    #     response.write(cookes["t1"])
    #
    # # response.set_cookie("t1","abc")
    # return response
    # 重定向过来的值
    # return HttpResponseRedirect("/bookApp/cookTest2")
    """等价于=="""
    return redirect("/bookApp/cookTest2")


def cookTest2(request):
    # cookes = request.COOKIES
    # response = HttpResponse()
    # if "t1" in cookes:
    #     response.write(cookes["t1"])
    #
    # # response.set_cookie("t1","abc")
    # return response
    return HttpResponse("这是重定向过来的值~~")


# 通过用户登录练习 sessions

def userLoginMain(request):
    name = request.session.get("myname","未登录")

    content = {
        "name": name
    }
    # 注意加/ 不加斜杠还是有区别的
    return render(request, "bookapp/userLoginMain.html", content)


# 用户登录页面
def sessionUserLogin(request):
    # 注意加/ 不加斜杠还是有区别的
    return render(request, "bookapp/userLogin.html")


# 用户登录
def sessionUserLoginHandler(request):
    # userName = request.POST["uname"]
    userName = request.POST["uname"]
    request.session["myname"] = userName
    request.session.set_expiry(10)
    # 注意加/ 不加斜杠还是有区别的
    return redirect("/bookApp/sessionUserMain/")


# 用户退出
def sessionUserLogout(request):
    # 删除sessions
    del request.session["myname"]
    # 注意加/ 不加斜杠还是有区别的
    return redirect("/bookApp/sessionUserMain/")

from django.shortcuts import render
from django.http import *
from django.conf import settings
import os


# Create your views here.

def index(request):
    return HttpResponse("卡卡罗特")
    # return render(request,"fileupapp/acessStaticFile.html")


#  访问静态文件
def acessStaticFile(request):
    return render(request, "fileupapp/acessStaticFile.html")


def MyExceptionTest(request):
    a1 = int("123a")
    # return render(request, "fileupapp/acessStaticFile.html")
    return HttpResponse("卡卡罗特")


# 上传文件的实例代码

def uploadFiles(request):
    return render(request, "fileupapp/uploadFiles.html")


# 执行返回结果
def uploadHandle(request):
    if request.method == "POST":
        f1 = request.FILES['uploadFile']
        # fname = '%s/fileUpApp/%s'%()
        fname = os.path.join(settings.MEDIA_ROOT, f1.name)
        with open(fname, 'wb+') as pic:
            for file in f1.chunks():
                pic.write(file)
    # return render(request,"fileupapp/uploadFiles.html")

    # return HttpResponse(fname)
    # return HttpResponse('<img src="/static/media/%s"/>'%f1.name)
    return HttpResponse('<img src="%smedia/%s"/>'%(settings.STATIC_URL,f1.name))

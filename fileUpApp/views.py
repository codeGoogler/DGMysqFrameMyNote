from django.shortcuts import render
from django.http import *
from django.conf import settings

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
    return render(request,"fileupapp/uploadFiles.html")

#执行返回结果
def uploadHandle(request):
    if  request.method == "POST":
        f1 = request.FILES['uploadFile']
        fname = '%s/fileUpApp/%s'%(settings.MEDIA_ROOT,f1.name)
        with open(fname,"w") as  pic:
            for file in f1.chunks():
                pic.write(file)
    # return render(request,"fileupapp/uploadFiles.html")

    return HttpResponse(fname)
    return HttpResponse('<img src="/static/medis/%s"%f1,name />')
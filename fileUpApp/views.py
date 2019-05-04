from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import *
from django.conf import settings
import os

from fileUpApp import models
from .models import UserInfo, Page


# Create your views here.

def index(request):
    # return HttpResponse("卡卡罗特")
    return render(request,"index.html")


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
    return HttpResponse('<img src="%smedia/%s"/>' % (settings.STATIC_URL, f1.name))


# 执行分页加载
def queryByPageMainTest(request, pageNo):
    try:
        print("传回的值为：%s" % pageNo)
        list = UserInfo.objects.all()
        print("list")
        print(list)
        paginator = Paginator(list, 7)
        print("paginator")
        print(paginator)
        perList = paginator.page(pageNo)
        print("perList")
        print(perList)
        content = {
            'perList': perList,
        }
        print(content)
        return render(request, "fileupapp/分页加载.html", content)
    except Exception  as e:
        print("粗错啦~~~~~ %s" % e)
        return render(request, "erro404.html")


def books(request):
    # 从url中获取当前页码数
    current_page = 1
    try:
        current_page = int(request.GET.get('page'))
    except Exception as e:
        current_page = 1

    # 总数量
    total_count = models.UserInfo.objects.count()

    # 每页数量
    per_count = 10

    # 总页数
    total_page, more = divmod(total_count, per_count)
    if more:
        total_page += 1

    # 每页显示最大页码数,(左右对称定义奇数)
    max_page_num = 11
    half_page_num = max_page_num // 2

    # 计算当前页面的页码范围
    if max_page_num >= total_page:
        # 总页码书小于最大显示页码数
        start_page = 1
        end_page = total_page
    elif current_page + half_page_num >= total_page:
        # 右边越界
        end_page = total_page
        start_page = total_page - max_page_num
    elif current_page - half_page_num <= 1:
        # 左边越界
        start_page = 1
        end_page = max_page_num
    else:
        # 正常状态
        start_page = current_page - half_page_num
        end_page = current_page + half_page_num

    start_index = (current_page - 1) * per_count
    end_index = current_page * per_count

    book_list = models.UserInfo.objects.all()[start_index:end_index]

    page_html_list = []

    # 加首页页码
    first_li = '<li><a href="/books/?page=1">首页</a></li>'
    page_html_list.append(first_li)

    # 加上一页页码
    if current_page == 1:
        prev_li = '<li class="disabled"><a href="#"><span aria-hidden="true">&laquo;</span></a></li>'
    else:
        prev_li = '<li><a href="/books/?page={}"><span aria-hidden="true">&laquo;</span></a></li>'.format(
            current_page - 1)
    page_html_list.append(prev_li)

    # 加中间页码
    for i in range(start_page, end_page + 1):
        if i == current_page:
            li = '<li class="active"><a href="/books/?page={0}">{0}</a></li>'.format(i)
        else:
            li = '<li><a href="/books/?page={0}">{0}</a></li>'.format(i)
        page_html_list.append(li)

    # 加下一页页码
    if current_page == total_page:
        next_li = '<li class="disabled"><a href="#"><span aria-hidden="true">&raquo;</span></a></li>'
    else:
        next_li = '<li><a href="/books/?page={}"><span aria-hidden="true">&raquo;</span></a></li>'.format(
            current_page + 1)
    page_html_list.append(next_li)

    # 加尾页页码
    end_li = '<li><a href="/books/?page={}">尾页</a></li>'.format(total_page)
    page_html_list.append(end_li)
    html_page = ''.join(page_html_list)

    return render(request, 'books.html', {'book_list': book_list, 'html_page': html_page})


def books(request):
    current_page = int(request.GET.get('page'))
    total_count = models.UserInfo.objects.count()
    page_obj = Page(current_page, total_count, request.path_info)
    userInfo_list = models.UserInfo.objects.all()[page_obj.start:page_obj.end]
    page_html = page_obj.page_html()
    return render(request, 'books.html', {'book_list': userInfo_list, 'html_page': page_html})

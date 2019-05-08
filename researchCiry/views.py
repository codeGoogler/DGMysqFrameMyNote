from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from researchCiry.models import AreaInfo
from . import models


# Create your views here.

def showAll2(request):
    return render(request, "researchciry/showall.html")


def showAll(request):
    try:
        print("================我要查询数据啦===============")
        allList = AreaInfo.objects.all()
        paginator = Paginator(allList, 10)
        showAll = paginator.page(1)
        content = {
            "showAll": showAll,
            "note": "================我要查询数据啦===============",
        }
        print("================我要查询数据啦===============allList:")
        print(allList)
        return render(request, "researchciry/showall.html", content)
    except Exception as e:
        print(e)
        content = {
            "showAll": "123",
            "note": e,
        }
        return render(request, "404.html", content)

# c查询所有的省
def area(request, index):
    pageNo = int(index)
    if pageNo == 0:
        content = AreaInfo.objects.filter(parea__isnull=True)
    else:
        content = AreaInfo.objects.filter(parea__isnull=True)
    # print(content)
    list = []
    for m in content:
        # print(m.title)
        list.append([m.id,m.title])
    data = {
        'data': list
    }
    # print(data)
    return JsonResponse(data)

# 查询所有的城市
def city(request ,provinceId):
    cityList = AreaInfo.objects.filter(parea_id=provinceId)
    list = []
    for model in  cityList:
        list.append({'id':model.id,'title':model.title})
    cirtData = {
        'cityData':list
    }
    return JsonResponse(cirtData)

# 查询所有的城市
def distance(request ,distanceId):
    cityList = AreaInfo.objects.filter(parea_id=distanceId)
    list = []
    for model in  cityList:
        list.append({'id':model.id,'title':model.title})
    distanceData = {
        'distanceData':list
    }
    return JsonResponse(distanceData)


# 自定义 编辑器
def cumtomerEdit(request):
    return render(request,"researchciry/cumtomerEdit.html")
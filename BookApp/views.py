from django.shortcuts import render
from django.db.models import Max, F, Q
# Create your views here.
from .models import  *

def show(request):

    bookInfo = BookInfo.bookManager.all()
    maxBookInfo = BookInfo.bookManager.aggregate(Max("bpub_date"))
    maxGt100BookInfo = BookInfo.bookManager.filter(breadnum__gt=100)# 查询月大量大于100的
    maxGtBookInfo1 = BookInfo.bookManager.filter(breadnum__gt=F("bcomment") * 5)# 查询月大量大于评论书的
    maxGtBookInfo2 = BookInfo.bookManager.filter(breadnum__gt=100,btitle__contains='贝')# 查询月大量大于评论书的
    maxGtBookInfo2 = BookInfo.bookManager.filter(breadnum__gt=100).filter(btitle__contains='贝')
    maxGtBookInfo3 = BookInfo.bookManager.filter(Q(btitle__contains='贝')|Q(isDelete=0))# 查询名字包含贝切isDelete=0的数据信息
    print("*" * 15)
    print(maxBookInfo)
    print(bookInfo)
    print(maxGtBookInfo1)

    content = {
        "title":"卡卡罗特",
        'bookList':bookInfo,
        'maxBookInfo':maxBookInfo,
        'maxGt100BookInfo':maxBookInfo,
        'maxGtBookInfo1':maxGtBookInfo1,
        'maxGtBookInfo2':maxGtBookInfo2,
        'maxGtBookInfo3':maxGtBookInfo3,
    }


    return render(request, 'bookapp/index.html', content)
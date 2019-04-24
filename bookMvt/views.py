from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def Test(request):
    return render(request, "bookapp/index.html")


# 用于extends 集成模板的学习
def showIndex(request):
    return render(request, "bookmvt/index.html")


def showUser1(request):
    return render(request, "bookmvt/user1.html")


def showUser2(request):
    return render(request, "bookmvt/user2.html")


# 用于html的转义

def htmlChangeTest(request):
    content = {
        "t1": "<h1>htmlChangeTest</h1>",
        "t2": "<h1>htmlChangeTest123</h1>"
    }
    return render(request, "bookmvt/htmlChangeTest.html", content)


# csrf的学习---》跨站请求伪造
def csrfRequestTest(request):
    return render(request, "bookmvt/csrfRequestTest.html")


def csrfResponseTest(request):
    uname = request.POST['uname']
    upwd = request.POST['upwd']
    print("登陆用户名：%s ,用户名密码：%s" % (uname, upwd))
    content = {
        "uname": uname,
        "upwd": upwd,
    }
    return render(request, "bookmvt/csrfResponseTest.html", content)


# 验证码的学习
# 可以参考 ： https://blog.csdn.net/samtaoys/article/details/52025859
def vetifyCodeTest(request):
    from PIL import Image, ImageDraw, ImageFont
    import random, math, io
    from io import StringIO, BytesIO
    # 创建背景颜色
    bgColor = (random.randrange(20, 200), random.randrange(20, 200), 255)
    # 规定宽高
    width = 150
    height = 50

    # 构造字体对象
    # font= ImageFont.truetype('FreeMono.ttf',23)
    font = ImageFont.truetype('simsun.ttc', 23)
    # font= ImageFont.truetype('Hiragino Sans GB.ttc',23)
    # 创建一个画布
    iamge = Image.new("RGB", (width, height), bgColor)
    # 创建一个画笔
    draw = ImageDraw.Draw(iamge)
    # 常见文本内容
    text = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"
    # 逐个绘制
    count = 4
    x = math.floor(width / count)/2-5
    y = 10
    textTemp = ''
    for it in range(count):
        subTextTemp = text[random.randrange(0, len(text))]
        textTemp += subTextTemp
        draw.text((x, y), subTextTemp, (255, 255, 255), font)
        x = x + math.floor(width / count)
    print(textTemp)
    # draw.text((x, y), text,(255,255,255),font)
    # 保存到内存之中
    # buffer = io.StringIO()
    buffer = BytesIO()
    iamge.save(buffer, "png")
    # 请内存中的内存流 输出到客户端
    # request.session["vertifyCode"] = textTemp
    request.session['vertifyCode'] = textTemp
    #释放画笔
    del  draw
    return HttpResponse(buffer.getvalue(), "image/png")


def vetifyCodeTest1(request):
    content = {}
    return render(request, "bookmvt/vetifyCodeTest1.html")


def verifyCodeResponseTest(request):
    code1 = request.POST["code"]
    vertifyCode = request.session["vertifyCode"]
    print("code1 :%s ， vertifyCode: %s"%(code1,vertifyCode))
    if vertifyCode == code1:
        responseResult = "ok"
        return HttpResponse(responseResult)
    else:
        responseResult = "false"
        return HttpResponse(responseResult)

if __name__ == "__main__":
    pass
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


# class MyException(MiddlewareMixin):
#     def process_exception(request, response, exception):
#         print(help(exception))
#         # print("我出现错误啦----->%s"%exception)
#         # return HttpResponse("数据转化异常~----->%s"%(exception))
#         return HttpResponse(exception)


class MyException(MiddlewareMixin):
    def process_exception(request, response, exception):
        print(help(exception))
        # print("我出现错误啦----->%s"%exception)
        return HttpResponse("数据转化异常~----->%s"%(exception))
        # return HttpResponse(exception)
#
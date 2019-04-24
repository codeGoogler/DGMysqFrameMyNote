# encoding=utf-8
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^Test/",views.Test),
    url(r"^showIndex/$",views.showIndex,name="showIndex"),
    url(r"^showUser1/$",views.showUser1,name="showUser1"),
    url(r"^showUser2/$",views.showUser2,name="showUser2"),
    url(r"^htmlChangeTest/$",views.htmlChangeTest,name="htmlChangeTest"),
    url(r"^csrfRequestTest/$",views.csrfRequestTest,name="csrfRequestTest"),
    url(r"^csrfResponseTest/$",views.csrfResponseTest,name="csrfResponseTest"),
    url(r"^vetifyCodeTest/$",views.vetifyCodeTest,name="vetifyCodeTest"),
    url(r"^vetifyCodeTest1/$",views.vetifyCodeTest1,name="vetifyCodeTest1"),
    url(r"^verifyCodeResponseTest/$",views.verifyCodeResponseTest,name="verifyCodeResponseTest"),


]

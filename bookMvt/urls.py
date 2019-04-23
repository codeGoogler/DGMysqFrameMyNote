# encoding=utf-8
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^Test/",views.Test),
    url(r"^showIndex/$",views.showIndex,name="showIndex"),
    url(r"^showUser1/$",views.showUser1,name="showUser1"),
    url(r"^showUser2/$",views.showUser2,name="showUser2"),
    url(r"^htmlChangeTest/$",views.htmlChangeTest,name="htmlChangeTest"),


]

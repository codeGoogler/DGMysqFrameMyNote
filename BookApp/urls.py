from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r"^$", views.show),
    url(r'^(\d+)/$', views.index),
    # url(r'^(\d+)/(\d+)/(\d+)/$', views.details),
    url(r'^(?P<p1>\d+)/(?P<p2>\d+)/(?P<p3>\d+)/$', views.details),
    path('error/', views.error),
    url(r'^getTest/$', views.getTest),
    url(r'^getTest1/$', views.getTest1),
    url(r'^getTest2/$', views.getTest2),
    # r 表示开始匹配，
    url(r'^postTest1/$', views.postTest1),
    url(r'^postTest2/$', views.postTest2),
    url(r'^cookTest1/$', views.cookTest1),
    url(r'^cookTest2/$', views.cookTest2),
    url(r'^sessionUserMain/$', views.userLoginMain),
    url(r'^sessionUserLogin/$', views.sessionUserLogin),
    url(r'^sessionUserLoginHandler/$', views.sessionUserLoginHandler),
    url(r'^sessionUserLogout/$', views.sessionUserLogout),


]

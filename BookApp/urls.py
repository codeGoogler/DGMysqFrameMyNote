from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$", views.show),
    url(r'^(\d+)/$', views.index),
    # url(r'^(\d+)/(\d+)/(\d+)/$', views.details),
    url(r'^(?P<p1>\d+)/(?P<p2>\d+)/(?P<p3>\d+)/$', views.details)

]

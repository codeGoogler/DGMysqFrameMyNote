from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^showAll/$',views.showAll,name="showAll"),
    url(r'^area/(\d+)/$',views.area),


]
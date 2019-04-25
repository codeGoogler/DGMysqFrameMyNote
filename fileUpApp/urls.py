from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    url("index", views.index),
    url("acessStaticFile", views.acessStaticFile,name='acessStaticFile'),
    url(r"^MyExceptionTest/$", views.MyExceptionTest,name='MyExceptionTest'),
    url(r"^uploadHandle/$", views.uploadHandle,name='uploadHandle'),
    url(r"^uploadFiles/$", views.uploadFiles,name='uploadFiles'),

]

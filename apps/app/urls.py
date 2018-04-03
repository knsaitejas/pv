from django.shortcuts import render, redirect
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^home/$', views.home),
]

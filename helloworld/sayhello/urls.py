from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail', views.detail, name='detail'),
    url(r'^execpy', views.execpy, name='execpy'),
    url(r'^classfy', views.classfy, name='classfy'),
]
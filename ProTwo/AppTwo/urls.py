from django.conf.urls import url
from django.contrib import admin
from AppTwo import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^help/', views.help,name='help'),

]

from django.conf.urls import url
from django.contrib import admin
from AppTwo import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^help/', views.help,name='help'),
    url(r'^users/', views.users,name='users'),
    url(r'^new_page/', views.new_page,name='new_page'),
    url(r'^form_page/', views.form_name_view,name='form_name_view'),

]

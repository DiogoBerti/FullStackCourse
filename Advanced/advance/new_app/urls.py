from django.conf.urls import url
from new_app import views

app_name = 'new_app'

urlpatterns = [
    url(r'ˆ$', views.SchoolList.as_view(),name='list'),



]

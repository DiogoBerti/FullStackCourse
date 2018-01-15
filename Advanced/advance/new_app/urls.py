from django.conf.urls import url
from new_app import views

app_name = 'new_app'

urlpatterns = [
    url(r'ˆ$', views.SchoolList.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/$', views.SchoolDetailView.as_view(), name='detail'),
    url(r'^create/$', views.SchoolCreateView.as_view(), name='create')
]

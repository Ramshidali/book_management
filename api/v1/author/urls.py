from django.urls import path, re_path
from . import views

app_name = 'api_v1_author'

urlpatterns = [
    re_path(r'^create/$', views.create_author),
    re_path(r'^list/$', views.author_list),
]

from django.urls import path, re_path

from rest_framework_simplejwt.views import (TokenRefreshView,)

from . import views

app_name = 'api_v1_authentication'

urlpatterns = [
    re_path(r'^token/$', views.UserTokenObtainPairView.as_view(), name='token_obtain_pair'),
    re_path(r'^token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    
    re_path(r'^signup/$', views.register),
    re_path(r'^signin/$', views.login),
    # re_path(r'^list/$', views.author_list),
]

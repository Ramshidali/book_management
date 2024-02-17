from django.urls import path, re_path
from . import views

app_name = 'api_v1_book'

urlpatterns = [
    re_path(r'^create/$', views.create_book),
    re_path(r'^list/$', views.book_list),
    re_path(r'^update/(?P<pk>.*)/$', views.update_book),
    re_path(r'^delete/(?P<pk>.*)/$', views.delete_book),
    
    re_path(r'^create-review/$', views.create_reviews),
    re_path(r'^reviews-list/$', views.reviews_list),
    re_path(r'^update-review/(?P<pk>.*)/$', views.update_reviews),
    re_path(r'^delete-review/(?P<pk>.*)/$', views.delete_reviews),
]

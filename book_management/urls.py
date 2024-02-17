from django.contrib import admin
from django.urls import  include, path, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/v1/authentication/', include(('api.v1.authentication.urls','authentication'), namespace='api_v1_authentication')),
    path('api/v1/author/', include(('api.v1.author.urls','author'), namespace='api_v1_author')),
    path('api/v1/book/', include(('api.v1.book.urls','book'), namespace='api_v1_book')),
]

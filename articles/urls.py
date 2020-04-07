from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    
    url(r'^$',views.article_list),
]

urlpatterns += staticfiles_urlpatterns()
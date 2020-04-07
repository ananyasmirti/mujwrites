from django.conf.urls import url,include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home),
    url(r'^team/$',views.team),
    url(r'^contact/$',views.contact),
    url(r'^category/$',views.category),
    url(r'^article/$',include('articles.urls')),
   
    
]
urlpatterns += staticfiles_urlpatterns()
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^account_slug/', include('account_slug.urls', namespace='account_slug')),
    url(r'^account_cbv/', include('account_cbv.urls', namespace='account_cbv')),
    url(r'^$', views.home, name='home')
]

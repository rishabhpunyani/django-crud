from django.conf.urls import url

from account_slug import views

urlpatterns = [
  url(r'^$', views.AccountList.as_view(), name='account_list'),
  url(r'^create/$', views.AccountCreate.as_view(), name='account_create'),
  url(r'^edit/(?P<slug>[\w-]+)/$', views.AccountUpdate.as_view(), name='account_edit'),
  url(r'^delete/(?P<slug>\w+)/$', views.AccountDelete.as_view(), name='account_delete'),
  url(r'^detail/(?P<slug>\w+)/$', views.AccountDetail.as_view(), name='account_detail'),
]

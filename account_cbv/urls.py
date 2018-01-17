from django.conf.urls import url

from account_cbv import views

urlpatterns = [
  url(r'^$', views.AccountList.as_view(), name='account_list'),
  url(r'^create$', views.AccountCreate.as_view(), name='account_create'),
  url(r'^edit/(?P<pk>\d+)$', views.AccountUpdate.as_view(), name='account_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.AccountDelete.as_view(), name='account_delete'),
  url(r'^detail/(?P<pk>\d+)$', views.AccountDetail.as_view(), name='account_detail'),

]

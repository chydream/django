from django.conf.urls import url

from accounts import views

urlpatterns = [
    # url(r'^login/$', views.page_login, name=']'),
    url(r'^user/login/$', views.user_login, name='user_login'),
    url(r'^user/logout/$', views.user_logout, name='user_logout'),
    url(r'^user/register/$', views.user_register, name='user_register'),
    url(r'^user/address/list$', views.address_list, name='address_list'),
    url(r'^user/address/edit/(?P<pk>\S+)/$', views.address_edit, name='address_edit'),
    url(r'^user/address/delete/(?P<pk>\d+)/$', views.address_delete, name='address_delete'),
]
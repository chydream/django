from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from mine import views

urlpatterns=[
    url(r'^order/detail/(?P<sn>\S+)/$', login_required(views.OrderDetailView.as_view()), name='order_detail'),
    url(r'^cart/add/(?P<prod_uid>\S+)/$', views.cart_add, name='cart_add'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^order/pay/$', views.order_pay, name='order_pay'),
    url(r'^$', views.index, name='index'),
    url(r'^order/list/', login_required(views.OrderListView.as_view()), name='order_list'),
    url(r'^prod/collect$', views.prod_collect, name='prod_collect'),
]
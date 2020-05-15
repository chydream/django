from django.conf.urls import url

from mall import views

urlpatterns=[
    # url(r'^pro/list/', views.pro_list, name='pro_list'),
    url(r'^pro/list/', views.ProductList.as_view(), name='pro_list'),
    url(r'^pro/load/list/', views.ProductList.as_view(
        template_name='product_load_list.html'
    ), name='product_load_list'),
    url(r'^pro/info/', views.pro_info, name='pro_info'),
]
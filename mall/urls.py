from django.conf.urls import url

from mall import views

urlpatterns=[
    url(r'^pro/list/', views.pro_list, name='pro_list'),
    url(r'^pro/info/', views.pro_info, name='pro_info'),
]
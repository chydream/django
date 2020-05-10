from django.conf.urls import url

from grade import views

urlpatterns = [
    url(r'^count/$', views.page_count, name='page_trans_hand')
]
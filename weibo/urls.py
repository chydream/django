from django.conf.urls import url

from weibo import views

urlpatterns = [
    url(r'^user/(?P<page>\d+)/$', views.page_user, name='page_user')
]
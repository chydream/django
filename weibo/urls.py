from django.conf.urls import url

from weibo import views

urlpatterns = [
    url(r'^user/(?P<page>\d+)/$', views.page_user, name='page_user'),
    url(r'^trans/$', views.page_trans, name='page_trans'),
    url(r'^trans_with/$', views.page_trans_with, name='page_trans_with'),
    url(r'^trans_hand/$', views.page_trans_hand, name='page_trans_hand'),
    url(r'^q/$', views.page_q, name='page_q'),
    url(r'^sql/$', views.page_sql, name='page_sql'),
    url(r'^sql2/$', views.page_sql2, name='page_sql2'),
    url(r'^comment/sql/$', views.page_comments, name='page_comments'),
]
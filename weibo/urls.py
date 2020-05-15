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
    url(r'^form/first/$', views.page_form_first, name='page_form_first'),
    url(r'^user/login/$', views.user_login, name='user_login'),
    url(r'^user/register/$', views.user_register, name='user_register'),
    url(r'^user/edit/$', views.user_edit, name='user_edit'),
    url(r'^file/upload/origin/$', views.file_upload_origin, name='file_upload_origin'),
    url(r'^file/upload/form/$', views.file_upload_form, name='file_upload_form'),
    url(r'^file/upload/weibo/$', views.file_upload_weibo, name='file_upload_weibo'),
]
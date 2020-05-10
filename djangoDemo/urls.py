"""djangoDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve

from . import views, settings

handler500 = 'djangoDemo.views.page_500'
handler404 = 'djangoDemo.views.page_404'



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', views.index),
    url(r'^$', views.index, name='index'),
    url(r'^index1/$', views.index_one, name='index_one'),
    url(r'^index2/$', views.index_two, name='index_two'),
    url(r'^print/request/$', views.print_request, name='print_request'),
    url(r'^print/res/$', views.print_res, name='print_res'),
    url(r'^print/json/$', views.print_json, name='print_json'),
    url(r'^print/attr/$', views.print_attr, name='print_attr'),
    url(r'^print/image/$', views.print_image, name='print_image'),
    url(r'^print/excel/$', views.print_excel, name='print_excel'),
    url(r'^article/(?P<year>[0-9]{4})/$', views.article, name='article_detail'),
    url(r'^auth/', include('oauth.urls', namespace='auth')),
    url(r'^mall/', include('mall.urls',namespace='mall')),
    url(r'^weibo/',include('weibo.urls',namespace='weibo')),
    url(r'^grade/',include('grade.urls',namespace='grade')),
    url(r'^templ/show/', views.templ_show, name='templ_show'),
]

# 添加自定义的静态资源
urlpatterns += [
    url(r'^medias/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT
    })
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns
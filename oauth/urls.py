from django.conf.urls import url

from oauth import views
urlpatterns = [
    url(r'^index/$', views.index, name="index"),
    url(r'^show/class/$', views.ShowClassView.as_view(), name='show_class'),
    url(r'^show/filter/$', views.show_filter, name='show_filter'),
]
from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from paste import views


urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(),  name='display_info'),
	url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='paste_detail'),
	url(r'^add/$', views.create_info, name='create_info'),
)

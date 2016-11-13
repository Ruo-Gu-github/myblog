from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from blogs.models import Blogspost
from blogs import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
    url(r'^(?P<blogs_id>\d+)/$', views.detail, name='detail'),
	# url(r'^$', views.listing, name='listing'),
)

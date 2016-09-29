from django.conf.urls import url

from . import views

app_name = "post"

urlpatterns = [
	# /posts/
	url(r'^$', views.index, name='index'),

	# /posts/1
	url(r'^(?P<post_id>[0-9]+)/$', views.post, name='post'),

	# /posts/new
	url(r'^new/$', views.CreatePost.as_view(), name="new"),
]
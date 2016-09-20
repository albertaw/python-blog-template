from django.conf.urls import url

from . import views

app_name = "post"

urlpatterns = [
	# /post/
	url(r'^$', views.index, name='index'),

	# /post/1
	url(r'^(?P<post_id>[0-9]+)/$', views.post),

	# /post/u
	url(r'^u/$', views.users),

	# /post/u/jane
	# using name groups for the url so that I can pass route parameters as keyword
	# arguments to the view. Ex. (?P<name>pattern), where name is the name of the group.
	# https://docs.djangoproject.com/en/1.10/topics/http/urls/
	url(r'^u/(?P<username>\w+)/$', views.user, name='user')
]
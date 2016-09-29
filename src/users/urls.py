from django.conf.urls import url
from . import views

app_name = 'users'

urlpatterns = [
    # /users
	url(r'^$', views.users, name='users'),

	# /users/jane
	# using name groups for the url so that I can pass route parameters as keyword
	# arguments to the view. Ex. (?P<name>pattern), where name is the name of the group.
	# https://docs.djangoproject.com/en/1.10/topics/http/urls/
	url(r'^(?P<username>\w+)/$', views.user, name='user')
]
from django.conf.urls import url

from . import views

app_name = "post"

urlpatterns = [
	# /post/
	url(r'^$', views.index, name='index'),	
]
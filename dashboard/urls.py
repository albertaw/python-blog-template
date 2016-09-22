from django.conf.urls import url
from . import views

app_name = 'dashboard'

urlpatterns = [
    # /dashboard
	url(r'^$', views.update_settings, name="index"),
    # /dashboard/update
    # url(r'^update/$', views.update_user, name="update")
    url(r'^update/$', views.update_settings, name="update")
]
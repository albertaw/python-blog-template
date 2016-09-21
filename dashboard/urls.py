from django.conf.urls import url
from . import views

app_name = 'dashboard'

urlpatterns = [
    # /dashboard
	url(r'^$', views.index, name="index"),
    # /dashboard/update
    url(r'^update/$', views.update_user, name="update")
]
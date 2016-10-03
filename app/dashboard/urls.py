from django.conf.urls import url
from . import views

app_name = 'dashboard'

urlpatterns = [
    # /dashboard
	url(r'^$', views.Dashboard.as_view(), name="index"),
]
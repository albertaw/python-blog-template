from django.conf.urls import url
from . import views

app_name = "auth"

urlpatterns = [
    url(r'^$', views.Login.as_view(), name='login'),
    url(r'^logout/', views.logout_user, name='logout'),
]

from django.conf.urls import url
from . import views

app_name = "auth"

urlpatterns = [
    # /auth
    url(r'^$', views.login_user, name='login'),
    #/auth/logout
    url(r'^logout/', views.logout_user, name='logout')
]

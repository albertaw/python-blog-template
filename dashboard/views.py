from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def index(request):
    if request.user.is_authenticated():
        return render(request, 'dashboard/index.html')
    else:
        return redirect('/posts/')
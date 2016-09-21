from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


# https://docs.djangoproject.com/en/1.10/topics/auth/default/#how-to-log-a-user-in
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/posts/')
    else:
        #context = {'error': 'Incorrect username password combination'}
        #return render(request, 'auth/login.html', context)
        #return HttpResponse("Invalid login details supplied.")

        return render(request, 'auth/login.html')

def logout_user(request):
    logout(request)
    return redirect('/posts/')
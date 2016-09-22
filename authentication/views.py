from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from forms import LoginForm

# https://docs.djangoproject.com/en/1.10/topics/auth/default/#how-to-log-a-user-in
'''
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard/')
    else:
        #context = {'error': 'Incorrect username password combination'}
        #return render(request, 'auth/login.html', context)
        #return HttpResponse("Invalid login details supplied.")

        return render(request, 'auth/login.html')
'''
def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return redirect('/dashboard/')
    else:
        form = LoginForm()
    return render(request, 'authentication/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('/posts/')
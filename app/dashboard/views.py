from django.shortcuts import render, redirect
from forms import DashboardForm
from django.contrib.auth.models import User
from django.views import View


class Dashboard(View):

    def get(self, request):
        form = DashboardForm()
        return render(request, 'dashboard/form.html', {'form': form})

    def post(self, request):
        form = DashboardForm(request.POST)
        user = request.user
        if form.is_valid():
            if form.has_changed():
                if form.cleaned_data['username']:
                    user.username = form.validate_username(user)
                if form.cleaned_data['email']:
                    user.email = form.cleaned_data['email']
                user.save()
            return redirect('/dashboard')
        return render(request, 'dashboard/form.html', {'form': form, 'user': user})


def index(request):
    if request.user.is_authenticated():
        return render(request, 'dashboard/form.html')
    else:
        return redirect('/posts/')

'''
def update_user(request):
    user = request.user
    username = request.POST['username'].strip()
    email = request.POST['email'].strip()
    old_password = request.POST['old-password'].strip()
    new_password = request.POST['new-password'].strip()
    new_password2 = request.POST['new-password2'].strip()


    if user.check_password(old_password):
        # send error message because passwords don't match
        context = {'message': 'old password not valid'}
        return redirect(request, 'dashboard/index.html')

    if username:
        user.username = username

    if email:
        user.email = email

    if new_password and (new_password == new_password2):
        user.set_password(new_password)
    else:
        # send error message that passwords do not match
        context = {'message': 'passwords not a match'}
        return render(request, 'dashboard/index.html', context)

    # update the account if everything checks out
    user.save()
    context = {'message': 'account updated'}
    return render(request, 'dashboard/index.html', context)
'''

# this is handling GET and POST requests
def update_settings(request):
    if request.method == 'POST':
        form = DashboardForm(request.POST)
        if form.is_valid():
            user = request.user
            user.username=form.cleaned_data['username']
            user.email=form.cleaned_data['email']
            user.save()
            return redirect('/dashboard')
    else:
        form = DashboardForm()
    return render(request, 'dashboard/form.html', {'form':form})
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def index(request):
    if request.user.is_authenticated():
        return render(request, 'dashboard/index.html')
    else:
        return redirect('/posts/')


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
def update_user(request):
    user = request.user
    username = request.POST['username']
    email = request.POST['email']
    old_password = request.POST['old-password']
    new_password = request.POST['new-password']
    new_password2 = request.POST['new-password2']
    # must enter valid password to update account
    if old_password == user.password:
        user.username = username
        if new_password & (new_password == new_password2):
            user.set_password(new_password)
        else:
            # send error message that passwords do not match
            context = {'message': 'passwords not a match'}
            return render(request, 'dashboard/index.html', context)
        # update the account
        user.save()
        context = {'message': 'account updated'}
        return render(request, 'dashboard/index.html', context)
    else:
        # send error message because passwords don't match
        context = {'message': 'old password not valid'}
        return render(request, 'dashboard/index.html')
'''
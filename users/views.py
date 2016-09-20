from django.shortcuts import render
from django.contrib.auth.models import User

def users(request):
	users = User.objects.all()
	context = {'users': users}
	return render(request, 'users/list.html', context)

def user(request, username):
	# get the user object that matches username
	user = User.objects.get(username=username)
	# get the posts for the user
	# Post.objects.filter(user__username=username)
	posts = user.post_set.all()
	# user object assigned to 'profile' to avoid conflicts with the user variable
	# for the logged in user
	context = {'profile': user, 'posts': posts}
	return render(request, 'users/detail.html', context)
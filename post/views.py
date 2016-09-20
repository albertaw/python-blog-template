from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Post

# Create your views here.


def index(request):
	posts = Post.objects.order_by('-created_at')
	context = {'posts': posts}
	return render(request, 'post/index.html', context)

def post(request, post_id):
	post = Post.objects.get(id=int(post_id))
	context = {'post': post}
	return render(request, 'post/post.html', context)

def users(request):
	users = User.objects.all()
	context = {'users': users}
	return render(request, 'post/users.html', context)

def user(request, username):
	# get the user object that matches username
	user = User.objects.get(username=username)
	# get the posts for the user
	# Post.objects.filter(user__username=username)
	posts = user.post_set.all()
	context = {'user': user, 'posts': posts}
	return render(request, 'post/user.html', context)
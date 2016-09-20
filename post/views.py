from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Post

# Create your views here.


def index(request):
	posts = Post.objects.order_by('-created_at')
	context = {'posts': posts}
	return render(request, 'post/list.html', context)

def post(request, post_id):
	post = Post.objects.get(id=int(post_id))
	context = {'post': post}
	return render(request, 'post/detail.html', context)

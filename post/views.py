from django.shortcuts import render
from .models import Post
# Create your views here.


def index(request):
	posts = Post.objects.order_by('-created_at')
	context = {'posts': posts}
	return render(request, 'post/index.html', context)
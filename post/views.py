from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Post
from .forms import PostForm

def index(request):
	posts = Post.objects.order_by('-created_at')
	context = {'posts': posts}
	return render(request, 'post/list.html', context)

def post(request, post_id):
	post = Post.objects.get(id=int(post_id))
	context = {'post': post}
	return render(request, 'post/detail.html', context)

def create_post(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request
		form = PostForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			post = Post(user=request.user, content=form.cleaned_data['content'])
			post.save()
			# redirect to a new URL:
			return redirect('/posts/new', message='Success!')

	# if a GET (or any other method) we'll create a blank form
	else:
		form = PostForm()

	# show the form
	return render(request, 'post/create_post.html', {'form': form})


from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Post
from .forms import PostForm

# Create your views here.


def PostListing(request):
    post_list = Post.objects.all()
    return render(request, 'post/post_list.html', {'posts': post_list})
    # return HttpResponse('<h1>Page was found</h1>')


def PostDetail(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except post.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'post/post_detail.html', {'post': post})


def Post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

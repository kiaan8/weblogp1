from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .form import NewPostForm
from django.shortcuts import get_object_or_404
from django.views import generic


# Create your views here.



def custom_404(request, e=None):
    print('helloo')
    return render(request, 'blog/404.html',status=404)



def post(request):
    posts = Post.objects.filter(status='pub').order_by('-datetime_modified')
    context = {
        'posts': posts
    }
    return render(request, 'blog/shiow_post.html', context)


def post_detil_view(request,pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
       return render(request,'blog/404_detail.html')
    return render(request,'blog/post_detail.html', {'post': post})


def post_add_view(request):
    if request.method == 'POST':
        form= NewPostForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('posts_list')
    else :
        form = NewPostForm()

    return render(request,'blog/add_post.html', context={'form':form})


def post_update_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = NewPostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return redirect('posts_list')

    return render( request, 'blog/add_post.html', context={'form': form} )


def post_delete_view(request, pk):
    post = get_object_or_404(Post,pk=pk)

    if request.method=="POST":
        post.delete()
        return redirect("post_list")


    return render(request, 'blog/post_delete.html', context={'post':post})



from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.contrib import messages

def index(request):
    context = {'posts':Post.objects.all()}
    return render(request, 'blogs/index.html',context)

def post(request,post_id):
    context = {'post':Post.objects.get(pk=post_id)}
    return render(request, 'blogs/post.html',context)

def create(request):
    form = CreatePostForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,'Post Added Succesfully')
        return redirect('blogs:index')
    context = {'form':form}
    return render(request, 'blogs/create.html',context)

def update(request,post_id):
    post = Post.objects.get(pk=post_id)
    form = CreatePostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request,'Post Update Successfully')
        return redirect('blogs:post',post_id)
    context = {'form':form}
    return render(request, 'blogs/create.html',context)

def delete(request,post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('blogs:index')
    
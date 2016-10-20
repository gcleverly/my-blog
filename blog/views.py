from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from .models import Post
from .forms import PostForm


def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "form":form,
    }
    return render(request, "blog/post_form.html", context)

def post_list(request):
    posts = Post.objects.all() #filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request,pk):
	post = get_object_or_404(Post,pk=pk)
	return render(request,'blog/post_detail.html',{'post':post})

def post_update(request, pk):
    instance = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        #message success
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "form": form,
        "title": instance.title,
        "instance":instance,
    }
    return render(request, 'blog/post_form.html', context)

def post_delete(request):
    return HttpRespose("<h1>Delete</h1>")



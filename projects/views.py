from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import messages

from .models import Project
from .forms import ProjectForm


def project_create(request):
    print("Files request:", request.FILES)
    print("Files post:", request.POST)

    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    form = ProjectForm(request.POST or None)

    if request.method == 'POST':


        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect(instance.get_absolute_url())

        context = {
            "form":form,
        }
        return render(request, "projects/project_form.html", context)


def project_detail(request,pk):
    project = get_object_or_404(Project,pk=pk)
    return render(request,'projects/project_detail.html',{'project':project})


def project_delete(request, pk):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Project, pk=pk)
    instance.delete()
    messages.success(request, "successfully deleted")


def project_list(request):
    projects = Project.objects.all() #filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'projects/project_list.html', {'projects': projects})


def project_update(request, pk):
    print("Files request:", request.FILES)
    print("Files post:", request.POST)
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Project, pk=pk)

    form = ProjectForm(request.POST or None, instance=instance)

    if request.method == 'POST':

        form = ProjectForm(request.POST, request.FILES,instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "form": form,
        "title": instance.title,
        "instance": instance,
        }
    return render(request, 'projects/project_form.html', context)

    #form = ProjectForm(request.POST or None, instance=instance)
    #if form.is_valid():
    #    instance = form.save(commit=False)
     #   instance.save()
        #message success
      #  return HttpResponseRedirect(instance.get_absolute_url())




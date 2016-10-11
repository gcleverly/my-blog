from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from .models import Project

def project_list(request):
    projects = Project.objects.all() #filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'projects/project_list.html', {'projects': projects})

def project_detail(request,pk):
	project = get_object_or_404(Project,pk=pk)
	return render(request,'projects/project_detail.html',{'project':project})



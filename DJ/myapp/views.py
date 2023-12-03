from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Project,Tag
from .forms import ProjectForm
from django.views.decorators.http import require_http_methods,require_POST,require_GET
# Create your views here.


def projects(request):
    projects= Project.objects.all()
    context= {'projects':projects }
    return render(request,"projects.html", context)



def project(request,pk):
    
    projectObj= Project.objects.get(id=pk)
    tags= projectObj.tags.all()
    context= {'projectObj':projectObj,'tags':tags}
    return render(request,"single-project.html",context)



def create_project(request):
    form= ProjectForm()
    if request.method=="POST":
        form=ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(projects)


    return render(request,'project_form.html',{'form':form})



def update_project(request):
    form= ProjectForm()
    if request.method=="POST":
        form=ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(projects)


    return render(request,'project_form.html',{'form':form})
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Project,Tag,Profile
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods,require_POST,require_GET
# Create your views here.


def projects(request):
    projects= Project.objects.all()
    context= {'projects':projects,'profile':Profile }
    return render(request,"projects.html", context)



def project(request,pk):
    
    projectObj= Project.objects.get(id=pk)
    tags= projectObj.tags.all()
    context= {'projectObj':projectObj,'tags':tags}
    return render(request,"single-project.html",context)


@login_required(login_url="login_user")
def create_project(request):
    form= ProjectForm()
    if request.method=="POST":
        form=ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(projects)


    return render(request,'project_form.html',{'form':form})


@login_required(login_url="login_user")
def update_project(request,pk):
    wanted_project= Project.objects.get(id=pk)
    form= ProjectForm(instance=wanted_project)
    if request.method=="POST":
        form=ProjectForm(request.POST,request.FILES,instance=wanted_project)
        if form.is_valid():
            wanted_project.title=f"{wanted_project.title} (updated)"
            wanted_project.save()
            form.save()
            return redirect(projects)
    return render(request,'project_form.html',{'form':form})
@login_required(login_url="login_user")
def delete_project(request,pk):
    wanted_project= Project.objects.get(id=pk)
    wanted_project.delete()
    return HttpResponse("The object is succesfully deleted")
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Project,Tag,Profile,Message
from .forms import ProjectForm,ReviewForm,MessageForm
from django.db.models import Q
from .utils import searchProject,paginate_projects
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods,require_POST,require_GET
# Create your views here.


def projects(request):
    
    projects,search_query= searchProject(request)
    page= request.GET.get('page')
    results=3
    projects,paginator,custom_range= paginate_projects(request,projects,results,page)
    context= {'projects':projects,'profile':Profile,'search_query':search_query,'paginator':paginator,'custom_range':custom_range }
    return render(request,"projects.html", context)
 


def project(request,pk):
    
    projectObj= Project.objects.get(id=pk)
    tags= projectObj.tags.all()
    projectObj.getVoteCount
    review_allowed= False
    try:
        all_reviews= (projectObj.review_set.all())
        review_profiles= []
        for test_review in all_reviews:
            print(test_review.owner)
            review_profiles.append((test_review.owner))
        
        if not request.user.profile in review_profiles:
            review_allowed=True
    except:
        review_allowed=True

        if projectObj.owner.user==request.user:
            print("yo chai ho yr bro")
  
    form= ReviewForm()
    if request.method=='POST' and review_allowed and request.user.is_authenticated:
        print(request.POST)
        form= ReviewForm(request.POST)
        form_instance= form.save(commit=False)
        form_instance.owner= request.user.profile
        form_instance.project= projectObj
        try:
            form_instance.save()
            messages.success(request, "Review Posted Successfully")
        except:
            messages.error(request, "Same user cannot place two reviews")
    context= {'projectObj':projectObj,'tags':tags,'form':form,'review_allowed':review_allowed}
    return render(request,"single-project.html",context)


@login_required(login_url="login_user")
def create_project(request):
    profile= request.user.profile
    form= ProjectForm()
    if request.method=="POST":
        form=ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project= form.save(commit=False)
            project.owner= profile
            project.save()
            return redirect(projects)


    return render(request,'project_form.html',{'form':form})


@login_required(login_url="login_user")
def update_project(request,pk):
    wanted_project= Project.objects.get(id=pk)
    if request.user==wanted_project.owner.user:
        form= ProjectForm(instance=wanted_project)
        if request.method=="POST":
            form=ProjectForm(request.POST,request.FILES,instance=wanted_project)
            if form.is_valid():
                wanted_project.title=f"{wanted_project.title} (updated)"
                wanted_project.save()
                form.save()
                return redirect(projects)
    else:
        return HttpResponse("You are not allowed to perform this action")
    return render(request,'project_form.html',{'form':form})
@login_required(login_url="login_user")
def delete_project(request,pk):
    wanted_project= Project.objects.get(id=pk)
    wanted_project.delete()
    return HttpResponse("The object is succesfully deleted")


@login_required(login_url="login_user")
def inbox(request):
    profile = request.user.profile
    messageRequests= profile.messages.all()
    unreadCount= messageRequests.filter(is_read=False).count()
    context= {'unreadCount':unreadCount,'messageRequests':messageRequests}
    return render(request,'inbox.html',context)


@login_required(login_url="login_user")
def messageContent(request,pk):
    reqMessage= Message.objects.get(id=pk)
    if request.user.profile == reqMessage.recepient:
        reqMessage.is_read=True
        reqMessage.save()
        context= {'reqMessage':reqMessage}
        return render(request,'message.html',context)
    else:
        return HttpResponse("You aren't allowed to view this message")




def sendMessage(request,pk):
    recipient= Profile.objects.get(id=pk)
    form= MessageForm()
    print(recipient)
    context={'form':form}
    
    if request.method=="POST":
        form = MessageForm(request.POST)
        form_instance= form.save(commit=False)
        form_instance.sender= request.user.profile
        form_instance.save()

    return render(request,"message_form.html",context)
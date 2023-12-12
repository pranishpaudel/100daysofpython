from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm,ProfileForm,SkillForm
from .models import User
from .models import Profile,Skill
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def profiles(request):
    profiles= Profile.objects.all()
    context = {'profiles':profiles}
    return render(request,'users/profiles.html',context)



def profile_user(request,pk):
    profile= Profile.objects.get(id=pk)
    # topskills= profile.skill_set.all()
    topskills= profile.skill_set.exclude(description_for_skill__exact='')
    otherskills = profile.skill_set.filter(description_for_skill='')
    print(otherskills)

    context= {'profile': profile,'skills': Skill.objects.all(),'topskills':topskills,'otherskills':otherskills}
    return render(request,'users/user-profile.html',context)

@login_required(login_url='login_user')
def userAccount(request):
    profile= request.user.profile
    skills= profile.skill_set.all()
    projects=profile.project_set.all()
    context={'profile':profile,'skills':skills,'projects':projects}
    return render(request,"users/account.html",context)

@login_required(login_url='login_user')
def editAccount(request,pk):
    wanted_object= Profile.objects.get(id=pk)
    form= ProfileForm(instance=wanted_object)
    context={'form':form}
    if  wanted_object==request.user.profile and request.user.id==wanted_object.user.id:
        if request.method=="POST":
            form= ProfileForm(request.POST,request.FILES,instance=wanted_object)
            form.save()
    else:
        return HttpResponse("Its not your profile to edit boiii")
    return render(request,"users/profile-form.html",context)
def login_user(request):
    page= True
    mariko=False
    if request.user.is_authenticated:
        return redirect("profiles")
    if request.method=="POST":
        username= request.POST.get("username")
        password= request.POST.get("password")
        print(username)
        print(password)

        try:
            user= User.objects.get(username=username)
            mariko= True
            print("User eXists")
        except:
            messages.error(request,"Username does not exist")
        if mariko:
            user= authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('profiles')
            else:
                messages.error(request,"Username or password does not match")
    
    

    return render(request,"users/login_register.html",{'page':page})



def logout_user(request):
    logout(request)
    return redirect("home")


def registerUser(request):
    page = False
    user_exists = False
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        
        # Check if the username already exists
        username = request.POST.get("username")
        if User.objects.filter(username=username).exists():
            user_exists = True
#http://127.0.0.1:8000/edit_account/8aa1781c-bfd2-4cbd-8b23-b125ad8cc359/
        if not user_exists:
            if form.is_valid():
                form.save()
                user = authenticate(username=username, password=request.POST.get("password1"))
                if user is not None:
                    login(request, user)
                    messages.success(request, "User account created and logged in successfully.")
                    return redirect('editAccount',pk=request.user.profile.id)
                else:
                    messages.error(request, "Failed to authenticate user after registration.")
            else:
                messages.error(request, "Form is invalid. Please check the provided information.")
        else:
            messages.error(request, "Username already exists in the database.")

    context = {'page': page, 'form': form}
    return render(request, "users/login_register.html", context)


@login_required(login_url="login_user")
def create_skill(request):
    form= SkillForm()
    context={'form':form}
    if request.method=="POST":
        form= SkillForm(request.POST)
        skill_form= form.save(commit=False)
        skill_form.owner= request.user.profile
        skill_form.save()
        return redirect(userAccount)
    return render(request,'users/skill_form.html',context)



@login_required(login_url="login_user")
def update_skill(request,pk):
    skill_object=Skill.objects.get(id=pk)
    if request.user.profile==skill_object.owner:
        form= SkillForm(instance=skill_object)
        context={'form':form}
        if request.method=="POST":
            form= SkillForm(request.POST,instance=skill_object)
            form.save()
            return redirect(userAccount)
    else:
        return HttpResponse("You are not allowed to update this skill")
    return render(request,'users/skill_form.html',context)


@login_required(login_url="login_user")
def delete_skill(request,pk):
    skill_object=Skill.objects.get(id=pk)
    if request.user.profile==skill_object.owner:
        print("USER IS AUTHORIZED")
        context={}
        if request.method=="POST":
            skill_object.delete()
            return redirect(userAccount)
    else:
        return HttpResponse("You are not allowed to update this skill")
    return render(request,"users/account.html",context)
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate,logout
from .models import User
from .models import Profile,Skill

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


def login_user(request):
    if request.user.is_authenticated:
        return redirect("profiles")
    if request.method=="POST":
        username= request.POST.get("username")
        password= request.POST.get("password")
        print(username)
        print(password)

        try:
            user= User.objects.get(username=username)
            print("User eXists")
        except:
            print("Username does not exist")

        user= authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('profiles')
    
    

    return render(request,"users/login_register.html")



def logout_user(request):
    logout(request)
    return redirect("home")


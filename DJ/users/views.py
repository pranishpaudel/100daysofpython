from django.shortcuts import render
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

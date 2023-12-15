from .models import Project,Tag,Profile
from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage



def searchProject(request):
    search_query=''
    if (request.GET.get("search_query")):
        search_query= (request.GET["search_query"])
    tags= Tag.objects.distinct().filter(name__icontains=search_query)
    projects= Project.objects.filter(Q(title__icontains=search_query)|
                                        Q(description__icontains= search_query)|
                                        Q(owner__name__icontains=search_query)|
                                        Q(tags__in=tags))
    return projects,search_query

def paginate_projects(request,projects,results,page):
    
    paginator= Paginator(projects,results)
    try:
        projects= paginator.page(page)
    except PageNotAnInteger:
        page=1
        projects= paginator.page(page)
    except EmptyPage:
        page= paginator.num_pages
        print(page)
        projects= paginator.page(page)
    
    leftIndex= (int(page)-1)
    if leftIndex<1:
        leftIndex=1
    rightIndex= (int(page)+2)
    if rightIndex>paginator.num_pages:
        rightIndex= paginator.num_pages+1

    custom_range= range(leftIndex,rightIndex)
    return projects,paginator,custom_range
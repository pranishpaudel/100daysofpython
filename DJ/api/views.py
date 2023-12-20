from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from .serializers import ProjectSerializer
from myapp.models import Project

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': 'api/projects'},
        {'GET': 'api/projects/id'},
        {'POST': 'api/projects/id/vote'},
        {'GET': 'api/users/token'},
    ]
    return Response(routes)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getProjects(request):
    print('User:',request.user)
    projects= Project.objects.all()
    serializer= ProjectSerializer(projects,many=True)
    return Response(serializer.data)



@api_view(['GET'])
def getProject(request,pk):
    project= Project.objects.get(id=pk)
    serializer= ProjectSerializer(project,many=False)
    return Response(serializer.data)



@api_view(["POST"])
@permission_classes([IsAuthenticated])
def projectVote(request,pk):
    project= Project.objects.get(id="17213ad2-7809-4881-adea-4ce610e65622")
    print(f"Data: {request.data}")
    vote_updated= project.review_set.all()
    for vote_update in vote_updated:
        vote_update= request.data['value']
    serializer= ProjectSerializer(project,many=False)
    return Response(serializer.data)
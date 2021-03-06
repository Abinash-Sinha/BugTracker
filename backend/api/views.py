from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import NewBug, NewProject
from .serializers import NewBugSerializer, NewProjectSerializer

@api_view(['GET', 'POST'])
def bug_list(request):
    if request.method == 'GET':
        data = NewBug.objects.all()

        serializer = NewBugSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = NewBugSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def bug_detail(request):
    try:
        newbug = NewBug.objects.all()
    except NewBug.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        newbug.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'GET':
        data = NewBug.objects.all()
        serializer = NewBugSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def new_proj(request):
    if request.method == 'POST':
        serializer = NewProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def view_proj(request):
    if request.method == 'GET':
        data = NewProject.objects.all()
        serializer = NewProjectSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

@api_view('GET')
def get_project(request):
    """
    get from project from db by project name or pk.
    """
    pass
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.middleware.csrf import get_token

from ..models.project import Project
from ..serializers import ProjectSerializer

class Projects (generics.ListCreateAPIView):
  def get(self, request):
    # index request
    # showing all projects owned by user
    projects = Project.objects.filter(owner=request.user.id)
    data = ProjectSerializer(projects, many=True).data
    return Response(data)

  serializer_class = ProjectSerializer
  def post(self, request):
    # Crete request

    request.data['project']['owner'] = request.user.id
    # Serialize/Create Project
    project = ProjectSerializer(data=request.data['project'])
    if project.is_valid():
      project.save()
      return Response(project.data, status=status.HTTP_201_CREATED)
    else:
      return Response(project.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
  def get(self, request, pk):
    project = get_object_or_404(Project, pk=pk)
    data = ProjectSerializer(project).data

    if not data['owner'] == request.user.id:
      raise PermissionDenied('Not your project. Permisison denied.')

    return Response(data)

  def delete(self, request, pk):
    # Delete request
    project = get_object_or_404(Project, pk=pk)
    data = ProjectSerializer(project).data
    if not data['owner'] == request.user.id:
      raise PermissionDenied('Permission denied. This is not your project.')
    else:
      project.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

  def partial_update(self, request, pk):
    # Update request
    if request.data['project'].get('owner', False):
      del request.data['project']['owner']

    project = get_object_or_404(Project, pk=pk)

    if not request.user.id == project.owner.id:
      raise PermissionDenied('Unauthorized, you do not own this project.')

    request.data['project']['owner'] = request.user.id

    ps = ProjectSerializer(project, data=request.data['project'])
    if ps.is_valid():
      ps.save()
      return Response(ps.data)
    return Response(ps.errors, status.HTTP_400_BAD_REQUEST)

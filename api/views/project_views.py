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

    if not project.owner.id == request.user.id:
      raise PermissionDenied('Not your project. Permisison denied.')

    return Response(data)

  def delete(self, request, pk):
    # Delete request
    project = get_object_or_404(Project, pk=pk)
    data = ProjectSerializer(project).data
    if not project.owner.id == request.user.id:
      raise PermissionDenied('Permission denied. This is not your project.')
    else:
      project.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

  def partial_update(self, request, pk):
      """Update Request"""
      # Remove owner from request object
      # This "gets" the owner key on the data['mango'] dictionary
      # and returns False if it doesn't find it. So, if it's found we
      # remove it.
      if request.data['project'].get('owner', False):
          del request.data['project']['owner']
      # Locate Mango
      # get_object_or_404 returns a object representation of our Mango
      project = get_object_or_404(Project, pk=pk)
      # Check if user is the same as the request.user.id
      if not request.user.id == project.owner.id:
          raise PermissionDenied('Unauthorized, you do not own this project')
      # Add owner to data object now that we know this user owns the resource
      request.data['project']['owner'] = request.user.id
      # Validate updates with serializer
      data = ProjectSerializer(project, data=request.data['project'])
      if data.is_valid():
          # Save & send a 204 no content
          data.save()
          return Response(status=status.HTTP_204_NO_CONTENT)
      # If the data is not valid, return a response with the errors
      return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)

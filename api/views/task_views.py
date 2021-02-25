from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.middleware.csrf import get_token

from ..models.task import Task
from ..serializers import TaskSerializer

class Tasks (generics.ListCreateAPIView):
  def get(self, request):
    # index request
    # showing all projects owned by user
    tasks = Task.objects.filter(owner=request.user.id)
    data = TaskSerializer(projects, many=True).data
    return Response(data)

  serializer_class = TaskSerializer
  def post(self, request):
    # Crete request

    request.data['task']['owner'] = request.user.id
    # Serialize/Create Project
    task = TaskSerializer(data=request.data['task'])
    if task.is_valid():
      task.save()
      return Response(task.data, status=status.HTTP_201_CREATED)
    else:
      return Response(task.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
  def get(self, request, pk):
    task = get_object_or_404(Task, pk=pk)
    data = TaskSerializer(task).data

    if not task.owner.id == request.user.id:
      raise PermissionDenied('Not your task. Permisison denied.')

    return Response(data)

  def delete(self, request, pk):
    # Delete request
    task = get_object_or_404(Task, pk=pk)
    data = TaskSerializer(task).data
    if not task.owner.id == request.user.id:
      raise PermissionDenied('Permission denied. This is not your task.')
    else:
      task.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

  def partial_update(self, request, pk):
      """Update Request"""
      # Remove owner from request object
      # This "gets" the owner key on the data['mango'] dictionary
      # and returns False if it doesn't find it. So, if it's found we
      # remove it.
      if request.data['task'].get('owner', False):
          del request.data['task']['owner']
      # Locate Mango
      # get_object_or_404 returns a object representation of our Mango
      task = get_object_or_404(Task, pk=pk)
      # Check if user is the same as the request.user.id
      if not request.user.id == task.owner.id:
          raise PermissionDenied('Unauthorized, you do not own this task')
      # Add owner to data object now that we know this user owns the resource
      request.data['task']['owner'] = request.user.id
      # Validate updates with serializer
      data = TaskSerializer(task, data=request.data['task'])
      if data.is_valid():
          # Save & send a 204 no content
          data.save()
          return Response(status=status.HTTP_204_NO_CONTENT)
      # If the data is not valid, return a response with the errors
      return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)

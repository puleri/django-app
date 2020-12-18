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
    project = ProjectSerializer(data=request.data)

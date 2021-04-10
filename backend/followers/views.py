from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes

from rest_framework.permissions import AllowAny, IsAuthenticated

from rest_framework.parsers import JSONParser

from .models import UserFollowing
from .serializers import FollowersSerializer

class FollowersViewSet(viewsets.ModelViewSet):

    queryset = UserFollowing.objects.all()
    serializer_class = FollowersSerializer
    permission_classes = [IsAuthenticated]


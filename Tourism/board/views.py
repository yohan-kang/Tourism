# Create your views here.
from django.conf import settings
from .models import Board, ReviewImg
from .serializers import BoardSerializer,ImgSerializer
from django.core.cache import cache
from rest_framework.permissions import IsAuthenticated

# --APIView(generics),permission case import add--
from rest_framework import generics,permissions,authentication

# custom permissions
from .permissions import IsReviewerEditorPermission


# unused
# from itertools import product
# from urllib import request
# from django.shortcuts import render
# from django.http import JsonResponse
# from rest_framework.response import Response
# from django.http import Http404

User = settings.AUTH_USER_MODEL

# class somethingAPIView(generics.RetrieveAPIView):
#     queryset = Board.objects.all()
#     serializer_class = BoardSerializer
# board_view = somethingAPIView.as_view()

class BoardAllList(generics.ListCreateAPIView):
  # authentication_classes = [authentication.SessionAuthentication]
  permission_classes = [IsReviewerEditorPermission]
  queryset = Board.objects.all()
  serializer_class = BoardSerializer

class BoardWriterList(generics.ListCreateAPIView):
  permission_classes = [permissions.IsAdminUser]
  # permission_classes = [permissions.DjangoModelPermissions ]
  serializer_class = BoardSerializer
  def get_queryset(self):
    user = self.request.user
    return Board.objects.filter(writer=user)
  def perform_create(self, serializer):
    serializer.save(writer=self.request.user)

class BoardDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = [IsAuthenticated]
  serializer_class = BoardSerializer
  def get_queryset(self):
    user = self.request.user
    return Board.objects.filter(writer=user)
  # If no data meets the criteria, you must return to the board list.

class BoardListCreateAPIViewt(generics.CreateAPIView):
  queryset = Board.objects.all()
  serializer_class = BoardSerializer
  # permission_classes = [IsTechnicianPermission]    # staff check

class BoardDetail2(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = [IsAuthenticated]
  queryset = Board.objects.all()
  serializer_class = BoardSerializer
  # lookup_field = 'username'

class BoardList2(generics.ListCreateAPIView):
  permission_classes = [IsAuthenticated]
  serializer_class = BoardSerializer
  def get_queryset(self):
    user = self.request.user
    return Board.objects.filter(writer=user)

  def perform_create(self, serializer):
    serializer.save(writer=self.request.user)



class BoardAllListAndImg(generics.ListAPIView):
  serializer_class = BoardSerializer
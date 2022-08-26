from itertools import product
from urllib import request
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from .models import Board
from .models import ReviewImg
from .serializers import BoardSerializer,ImgSerializer
from django.core.cache import cache
from rest_framework.permissions import IsAuthenticated

# --api_view case import add--
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.http import Http404

# --APIView(generics),permission case import add--
# from rest_framework.views import APIView
from rest_framework import generics,permissions,authentication
# from Tourism.board import serializers

# custom permissions
from .permissions import IsStaffEditorPermission, IsTechnicianPermission
# custom mixins
from .mixins import StaffEditorPermissionMixin


# class somethingAPIView(generics.RetrieveAPIView):
#     queryset = Board.objects.all()
#     serializer_class = BoardSerializer
# board_view = somethingAPIView.as_view()



class BoardAllList(generics.ListAPIView):
  queryset = Board.objects.all()
  serializer_class = BoardSerializer

class BoardWriterList(generics.ListCreateAPIView):
  permission_classes = [permissions.IsAdminUser,IsStaffEditorPermission]
  # permission_classes = [permissions.DjangoModelPermissions ]
  serializer_class = BoardSerializer
  def get_queryset(self):
    user = self.request.user
    return Board.objects.filter(writer=user)
  


class BoardDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = [IsAuthenticated]
  serializer_class = BoardSerializer



# class BoardListCreateAPIViewt(StaffEditorPermissionMixin,generics.ListCreateAPIView):  if use this don.t need permission_classes
class BoardListCreateAPIViewt(generics.ListCreateAPIView):
  queryset = Board.objects.all()
  serializer_class = BoardSerializer

  # I don't know it's necessary or not.
  # authentication_classes = [authentication.SessionAuthentication]
  # authentication_classes = [authentication.TokenAuthentication]
  # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  #eyelike v2 web, we need to think about what we need this for
  # permission_classes = [permissions.DjangoModelPermissions] # user private Permissions check
  permission_classes = [IsTechnicianPermission]    # staff check


class BoardDetail2(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = [IsAuthenticated,IsTechnicianPermission]
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
  # queryset = ReviewImg.objects.select_related('board').filter(user_id=2)
  queryset = Board.objects.all().select_related('ReviewImg').filter(id=2)


  # queryset = ReviewImg.objects.all()
  serializer_class = ImgSerializer
  # serializer_class = ImgSerializer
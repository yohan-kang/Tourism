from itertools import product
from urllib import request
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from .models import Board
from .serializers import BoardSerializer
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
from .permissions import IsStaffEditorPermission
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
  
  # how to use perform_create : 
  #def perform_create(self, serializer):
    ## serializer.save(writer=self.request.user)
    # print(serializer.validated_data)
    # title = serializer.validated_data.get('title')
    # content= serializer.validated_data.get('content') or None
    # if content is None:
    #     content = title
    # serializer.save(content= content)

class BoardDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = [IsAuthenticated]
  serializer_class = BoardSerializer
  # def get_queryset(self):
  #   user = self.request.user
  #   print(self.request.path_info)
  #   return Board.objects.filter(writer=user)


# class BoardListCreateAPIViewt(StaffEditorPermissionMixin,generics.ListCreateAPIView):  if use this don.t need permission_classes
class BoardListCreateAPIViewt(generics.ListCreateAPIView):
  queryset = Board.objects.all()
  serializer_class = BoardSerializer

  # I don't know it's necessary or not.
  # authentication_classes = [authentication.SessionAuthentication]
  # authentication_classes = [authentication.TokenAuthentication]
  # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  #eyelike v2 web, we need to think about what we need this for
  permission_classes = [permissions.DjangoModelPermissions] # user private Permissions check
  # permission_classes = [IsStaffEditorPermission]    # staff check


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













# # ---- use api_view case----

# def viewjson(request):
#     return JsonResponse("API base point...", safe=False)
# @api_view(['GET'])
# # @authentication_classes()
# # @permission_classes([IsAuthenticated])
# def index(request):
#     api_urls = {
#         'List': '/boardList/',
#         'Detail': '/boardView/<str:pk>/',
#         'Create': '/boardInsert/',
#         # 'Update': '/boardUpdate/<str:pk>/',
#         'Delete': '/boardDelete/<str:pk>/',
#     }
#     boards = Board.objects.all().order_by('id')

#     serializer = BoardSerializer(boards, many=True)

#     return Response(api_urls)


# @api_view(['GET'])
# # @permission_classes([IsAuthenticated])
# def boardList(request):

#     data = Board.objects.all().order_by('id')
#     serializer = BoardSerializer(data, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def userboardList(request):
#     if request.user.is_superuser : 
#       data = Board.objects.all().order_by('id')
#     else :
#       data = Board.objects.all().filter(accessUser=request.user).all()
#     serializer = BoardSerializer(data, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def boardInsert(request, *args, **kwargs):
#     serializer = BoardSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save(accessUser=request.user)
#         return Response(serializer.data, status=201)
#     return Response(serializer.errors, status=404)

# @api_view(['GET' ,'PUT','DELETE'])
# def boardView(request, pk):

#     try:
#         obj_data = Board.objects.get(pk=pk)
#     except obj_data.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     # Detail part
#     if request.method == 'GET':
#       serializer = BoardSerializer(obj_data)
#       return Response(serializer.data)

#     # Update part
#     elif request.method == 'PUT':
#         serializer = BoardSerializer(obj_data, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # Delete 
#     elif request.method == 'DELETE':
#         obj_data.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['DELETE'])
# def boardDelete(request, pk):
#     board = Board.objects.get(id=pk)
#     if board:
#         board.delete()

#     return Response("Deleted...")

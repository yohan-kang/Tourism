from urllib import request
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from .models import Board
from .serializers import BoardSerializer
from django.core.cache import cache
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

# --APIView case import add--
from rest_framework.views import APIView
from django.http import Http404
# from Tourism.board import serializers

# @permission_classes([IsAuthenticated])
class BoardAllList(APIView):

  # 
  def post(self, format=None):
    serializer = BoardSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

  #
  def get(self,request,format=None):
    queryset = Board.objects.all()
    serializer = BoardSerializer(queryset,many=True)
    return Response(serializer.data)




# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def userboardList(request):
#     if request.user.is_superuser : 
#       data = Board.objects.all().order_by('id')
#     else :
#       data = Board.objects.all().filter(accessUser=request.user).all()
#     serializer = BoardSerializer(data, many=True)
#     return Response(serializer.data)


class BoardWriterList(APIView):
  #
  def get(self,request,format=None):
    try:
        if request.user.is_superuser : 
          data = Board.objects.all().order_by('id')
        else :
          data = Board.objects.all().filter(writer=request.user).all()
        serializer = BoardSerializer(data, many=True)
        return Response(serializer.data)
    except data.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # queryset = Board.objects.all()
    # serializer = BoardSerializer(queryset,many=True)
    # return Response(serializer.data)

  # 
  def post(self, format=None):
    serializer = BoardSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

class BoardDetail(APIView):

    # purpose: When accessing the page, first check if there is data that meets the conditions.
    def get_object(self,request, pk):
      try:
        print("start get object-------------------------------------")
        print(request.user)
        return Board.objects.filter(writer=request.user,pk=pk)
        # return Board.objects.get(pk=pk)
      except Board.DoesNotExist:
        raise Http404

    # 
    def get(self,request,pk,format=None):
      print("request.user-------------------------------------")
      print(request.user)
      print(pk)
      post = self.get_object(pk)  #Board.objects.get(pk=pk)를 의미
      #  get_object() missing 2 required positional arguments: 'request' and 'pk'
      serializer = BoardSerializer(post)
      return Response(serializer.data)

    #
    def put(self,request,pk,format=None):
      post = self.get_object(pk)
      serializer = BoardSerializer(post, data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    # 
    def delete(self,request,pk,format=None):
      post =self.get_object(pk)
      post.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)


















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

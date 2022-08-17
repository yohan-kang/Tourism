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

def viewjson(request):
    return JsonResponse("API base point...", safe=False)


@api_view(['GET'])
# @authentication_classes()
# @permission_classes([IsAuthenticated])
def index(request):
    api_urls = {
        'List': '/boardList/',
        'Detail': '/boardView/<str:pk>/',
        'Create': '/boardInsert/',
        # 'Update': '/boardUpdate/<str:pk>/',
        'Delete': '/boardDelete/<str:pk>/',
    }
    boards = Board.objects.all()

    serializer = BoardSerializer(boards, many=True)

    return Response(api_urls)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def boardList(request):

    data = Board.objects.all()
    serializer = BoardSerializer(data, many=True)
    return Response(serializer.data)

    # data = cache.get_or_set('all_board',BoardSerializer(Board.objects.all(), many=True).data)
    # return Response(data)

@api_view(['POST'])
def boardInsert(request):
    serializer = BoardSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=404)
    # else:
    #     print("Invalid...")
    #     return (serializer.errors, status=status.HTTP_404_NOT_FOUND)
    # return Response(serializer.data, status=201)


@api_view(['GET' ,'PUT','DELETE'])
def boardView(request, pk):

    try:
        obj_data = Board.objects.get(pk=pk)
    except obj_data.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # Detail part
    if request.method == 'GET':
      serializer = BoardSerializer(obj_data)
      return Response(serializer.data)
    # data = cache.get_or_set(f'board:{pk}',BoardSerializer(Board.objects.get(id=pk), many=False).data)
    # return Response(data)

    # Update part
    elif request.method == 'PUT':
        serializer = BoardSerializer(obj_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete 
    elif request.method == 'DELETE':
        obj_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['PUT'])
# def boardUpdate(request, pk):
#     board = Board.objects.get(id=pk)
#     serializer = BoardSerializer(instance=board, data=request.data)

#     if serializer.is_valid():
#         print("Valid...")
#         serializer.save()
#         cache.set(f'board:{pk}',Board.objects.get(id=pk))
#     else:
#         print("Invalid...")

#     return Response(serializer.data)


@api_view(['DELETE'])
def boardDelete(request, pk):
    board = Board.objects.get(id=pk)
    if board:
        board.delete()

    return Response("Deleted...")

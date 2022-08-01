from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Board
from .serializers import BoardSerializer

def viewjson(request):
    return JsonResponse("API base point...", safe=False)


@api_view(['GET'])
def index(request):
    api_urls = {
        'List': '/boardlist/',
        'Detail': '/boardview/<str:pk>/',
        'Create': '/boardinsert/',
        'Update': '/boardupdate/<str:pk>/',
        'Delete': '/boarddelete/<str:pk>/',
    }

    boards = Board.objects.all()

    serializer = BoardSerializer(boards, many=True)

    return Response(api_urls)


@api_view(['GET'])
def boardList(request):

    boards = Board.objects.all()
    serializer = BoardSerializer(boards, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def boardView(request, pk):

    boards = Board.objects.get(id=pk)
    serializer = BoardSerializer(boards, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def boardInsert(request):
    serializer = BoardSerializer(data=request.data)

    if serializer.is_valid():
        print("Valid...")
        serializer.save()
    else:
        print("Invalid...")

    return Response(serializer.data)


@api_view(['PUT'])
def boardUpdate(request, pk):
    board = Board.objects.get(id=pk)
    serializer = BoardSerializer(instance=board, data=request.data)

    if serializer.is_valid():
        print("Valid...")
        serializer.save()
    else:
        print("Invalid...")

    return Response(serializer.data)


@api_view(['DELETE'])
def boardDelete(request, pk):
    board = Board.objects.get(id=pk)
    if board:
        board.delete()

    return Response("Deleted...")

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

def viewjson(request):
    return JsonResponse("API base point...", safe=False)


@api_view(['GET'])
# @authentication_classes()
@permission_classes([IsAuthenticated])
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
@permission_classes([IsAuthenticated])
def boardList(request):

    data = cache.get_or_set('all_board',BoardSerializer(Board.objects.all(), many=True).data)
    return Response(data)


@api_view(['GET'])
def boardView(request, pk):

    data = cache.get_or_set(f'board:{pk}',BoardSerializer(Board.objects.get(id=pk), many=False).data)
    return Response(data)


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
        cache.set(f'board:{pk}',Board.objects.get(id=pk))
    else:
        print("Invalid...")

    return Response(serializer.data)


@api_view(['DELETE'])
def boardDelete(request, pk):
    board = Board.objects.get(id=pk)
    if board:
        board.delete()

    return Response("Deleted...")

from django.http import JsonResponse 
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def getRoutes(requset):
    routes = [
        '/token',
        '/token/refresh'
    ]
    return Response(routes)

# from django.conf import settings
# from django.shortcuts import render
# from django.shortcuts import reverse
# from django.http import HttpResponse
# from django.http import Http404
# from allauth.account.views import PasswordChangeView
# from rest_framework import viewsets
# from rest_framework import serializers
# from accounts.models import User


# # Create your views here.
# def list(request):
#     # 로그인 상태 표시 : ㄴis_authenticated
#     if settings.DEBUG:
#         print(request.user.is_authenticated) 
#     return render(request,'tourism/list.html')

# class CustomPasswordChangeView(PasswordChangeView):
#     def get_success_url(self):
#       return reverse("list")

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = "__all__"
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
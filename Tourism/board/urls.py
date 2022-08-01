from django.conf.urls import url, include
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('viewjson/', views.viewjson, name="viewjson"),
    path('boardlist/', views.boardList, name="boardlist"),
    path('boardview/<str:pk>/', views.boardView, name="boardview"),
    path('boardinsert/', views.boardInsert, name="boardinsert"),
    path('boardupdate/<str:pk>/', views.boardUpdate, name="boardupdate"),
    path('boarddelete/<str:pk>/', views.boardDelete, name="boarddelete"),
]

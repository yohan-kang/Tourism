# from django.conf.urls import url, include
from django.urls import path, include

from . import views

urlpatterns = [
  # -- use APIView case --
  path('',views.BoardAllList.as_view()),
  path('writer/',views.BoardWriterList.as_view()),
  path('writer/<int:pk>/',views.BoardDetail.as_view())



    # -- use api_view case --

    # # path('', views.index, name="index"),
    # path('viewjson/', views.viewjson, name="viewjson"),
    # path('boardlist/', views.boardList, name="boardList"),
    # path('userboardlist/', views.userboardList, name="userboardList"),
    # path('boardview/<str:pk>/', views.boardView, name="boardView"),
    # path('boardinsert/', views.boardInsert, name="boardInsert"),
    # # path('boardupdate/<str:pk>/', views.boardUpdate, name="boardupdate"),
    # path('boarddelete/<str:pk>/', views.boardDelete, name="boardDelete"),
]

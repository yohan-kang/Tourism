# from django.conf.urls import url, include
from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
from . import views

urlpatterns = [
  # -- use APIView case --
  # path('',views.BoardAllList.as_view()),
  # path('add/',views.BoardListCreateAPIViewt.as_view()),
  # path('list/',views.BoardWriterList.as_view()), 
  # path('detail/<int:pk>/',views.BoardDetail.as_view()),
  path('',views.BoardList.as_view()),
  path('<int:pk>/',views.BoardDetail.as_view()),
  # path('img/',views.BoardAllListAndImg.as_view()),
] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

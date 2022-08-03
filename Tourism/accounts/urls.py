from django.urls import path, include
from . import views
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework_simplejwt import views as jwt_views
urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    # path('', views.list, name="list"),
    # path('login/', views.JWTLoginView.as_view(), name="list"),
    # path('signup/', views.JWTSignupView.as_view(), name="list"),
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
]
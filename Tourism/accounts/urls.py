from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    # path('', views.list, name="list"),
    # path('login/', views.JWTLoginView.as_view(), name="list"),
    # path('signup/', views.JWTSignupView.as_view(), name="list"),
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
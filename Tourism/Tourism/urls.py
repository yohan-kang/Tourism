from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
    path('boards/', include('board.urls')),
]

# from accounts import views 
# from django.views.generic import TemplateView
# from accounts.views import CustomPasswordChangeView
# from rest_framework import routers
# from accounts.views import UserViewSet

# router = routers.DefaultRouter()
# router.register('user', UserViewSet)
# urlpatterns = [
#     path('', include(router.urls)),
#     # admin
#     path('admin/', admin.site.urls),
#     # accounts
#     # path('accounts/', include('dj_rest_auth.urls')),
#     path('accounts/', include('dj_rest_auth.registration.urls')),
#     # path('accounts/', include('allauth.urls')),
#     path('accounts/', include('accounts.urls')),
#     #board
#     path("", include('board.urls')),
#     # allauth
#     path(
#       "email-confirmation-done/", 
#       TemplateView.as_view(template_name='Tourism/email_confirmation_done.html'),
#       name="account_email_confirmation_done",
#     ),
#     path(
#         'password/change/',
#         CustomPasswordChangeView.as_view(),
#         name="account_password_change"
#     ),
#     # list page
#     path('accommodation/', views.list),
# ]

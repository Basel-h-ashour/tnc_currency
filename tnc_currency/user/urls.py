from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import CreateUserView, ManageUserView

urlpatterns = [
    path('create/', CreateUserView.as_view(), name="create"),
    path('me/', ManageUserView.as_view(), name='me'),
    path('login/', TokenObtainPairView.as_view()),
    path('login/refresh', TokenRefreshView.as_view()),
]
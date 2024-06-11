from users.apps import UsersConfig
from rest_framework.routers import DefaultRouter
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.serializers import UserSerializer
from users.views import PaymentListAPIView, PaymentCreateAPIView, UserViewSet

app_name = UsersConfig.name

# router = DefaultRouter()
# router.register(r'users', UserViewSet, basename='courses')


urlpatterns = ([

    path('register/', UserSerializer, name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('payment/', PaymentListAPIView.as_view(), name='payment_list'),
    path('payment/create/', PaymentCreateAPIView.as_view(), name='payment_create'),


])
              # + router.urls

from rest_framework.permissions import AllowAny

from users.apps import UsersConfig

from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


from users.views import PaymentListAPIView, PaymentCreateAPIView, UserCreateAPIView

app_name = UsersConfig.name

urlpatterns = ([

    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('payment/', PaymentListAPIView.as_view(), name='payment_list'),
    path('payment/create/', PaymentCreateAPIView.as_view(), name='payment_create'),


])


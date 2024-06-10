from users.apps import UsersConfig
from rest_framework.routers import DefaultRouter
from django.urls import path

from users.views import PaymentListAPIView, PaymentCreateAPIView, UserViewSet

app_name = UsersConfig.name

# router = DefaultRouter()
# router.register(r'users', UserViewSet, basename='courses')


urlpatterns = ([
    path('payment/', PaymentListAPIView.as_view(), name='payment_list'),
    path('payment/create/', PaymentCreateAPIView.as_view(), name='payment_create'),

])
              # + router.urls

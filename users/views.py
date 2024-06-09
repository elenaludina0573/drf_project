from rest_framework import viewsets, generics

from users.models import Payment, User
from users.serializers import PaymentSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
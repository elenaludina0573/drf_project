from rest_framework import viewsets, generics
from rest_framework.filters import SearchFilter, OrderingFilter

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

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['paid_lesson', 'paid_course', 'payment_method']
    ordering_fields = ['-date_of_payment']

from rest_framework import serializers

from users.models import Payment
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def perform_create(self, serializer):
        user = serializer.save(is_activ=True)
        user.set_password(user.password)
        user.save()


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"

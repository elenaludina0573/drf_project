from django.contrib import admin
from users.models import User, Payment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['pk', 'email', 'is_active', 'is_staff', 'is_superuser']


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['pk', 'user', 'date_of_payment', 'paid_lesson', 'paid_course', 'payment_sum', 'payment_method']

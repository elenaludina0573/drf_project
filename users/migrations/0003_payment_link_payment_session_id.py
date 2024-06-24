# Generated by Django 5.0.6 on 2024-06-22 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='link',
            field=models.URLField(blank=True, max_length=400, null=True, verbose_name='Cсылка на оплату'),
        ),
        migrations.AddField(
            model_name='payment',
            name='session_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Id сессии'),
        ),
    ]
# Generated by Django 5.0.7 on 2024-11-23 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodHitchApp', '0049_message_customer_message_rider_order_paymentmethod_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]

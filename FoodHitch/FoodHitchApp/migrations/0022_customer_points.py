# Generated by Django 5.0.7 on 2024-09-17 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodHitchApp', '0021_delivery_restaurantid'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='Points',
            field=models.IntegerField(default=0),
        ),
    ]

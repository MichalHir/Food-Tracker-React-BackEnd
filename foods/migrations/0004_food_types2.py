# Generated by Django 5.1.4 on 2025-01-09 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("foodTypes", "0001_initial"),
        ("foods", "0003_alter_food_types"),
    ]

    operations = [
        migrations.AddField(
            model_name="food",
            name="types2",
            field=models.ManyToManyField(
                related_name="foods", to="foodTypes.food_type"
            ),
        ),
    ]

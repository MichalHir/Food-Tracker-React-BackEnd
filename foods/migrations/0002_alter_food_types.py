# Generated by Django 5.1.4 on 2025-01-09 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='types',
            field=models.ManyToManyField(related_name='foodTypes', to='foods.food_type'),
        ),
    ]
from django.db import models

from foodTypes.models import Food_type


# Create your models here.


class Food(models.Model):
    name = models.CharField(max_length=255)
    # types = models.ManyToManyField(
    #     Food_type, related_name="foods"
    # )  # Many-to-many relationship with Food_type
    typesOfFood = models.ManyToManyField(Food_type, related_name="foods")

    def __str__(self):
        return self.name

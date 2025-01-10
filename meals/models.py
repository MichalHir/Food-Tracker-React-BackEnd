from django.db import models

from foods.models import Food


# Create your models here.
class Meal(models.Model):
    # user = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING, related_name='user',null=True)
    date = models.DateField()
    time = models.TimeField()
    food_info = models.ManyToManyField(
        Food, related_name="meals"
    )  # Many-to-Many relationship with Food

    def __str__(self):
        return f"{self.time} - {self.food_info}"

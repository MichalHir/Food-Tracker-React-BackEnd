from django.shortcuts import render
from rest_framework import viewsets
from meals.models import Meal
from meals.serializers import MealSerializer


# Create your views here.
class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

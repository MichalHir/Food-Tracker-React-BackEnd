from django.shortcuts import render
from rest_framework import viewsets
from foods.models import Food, Food_type
from foods.serializers import FoodSerializer, FoodTypeSerializer


# Create your views here.
class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


# class FoodTypeViewSet(viewsets.ModelViewSet):
#     queryset = Food_type.objects.all()
#     serializer_class = FoodTypeSerializer

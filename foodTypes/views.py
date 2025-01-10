from django.shortcuts import render
from rest_framework import viewsets

from foodTypes.models import Food_type
from foodTypes.serializers import FoodTypeSerializer


# Create your views here.
class FoodTypeViewSet(viewsets.ModelViewSet):
    queryset = Food_type.objects.all()
    serializer_class = FoodTypeSerializer

from django.shortcuts import render
from rest_framework import viewsets
from meals.models import Meal
from meals.serializers import MealSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from meals.serializers import CustomTokenObtainPairSerializer


# Create your views here.
class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


class TokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

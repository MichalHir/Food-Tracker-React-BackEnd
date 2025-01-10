from django.shortcuts import render
from rest_framework import viewsets
from meals.models import Meal
from meals.serializers import MealSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from meals.serializers import CustomTokenObtainPairSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


class TokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


@api_view(["DELETE"])
def delete_meal(request, meal_id):
    try:
        meal = Meal.objects.get(id=meal_id)
        meal.delete()
        return Response({"message": "Meal deleted successfully"}, status=204)
    except Meal.DoesNotExist:
        return Response({"error": "Meal not found"}, status=404)

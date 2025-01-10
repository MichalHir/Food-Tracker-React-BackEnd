from foods.models import Food
from meals.models import Meal
from rest_framework import serializers


class MealSerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(queryset=MyUser.objects.all())
    food_info = serializers.PrimaryKeyRelatedField(
        queryset=Food.objects.all(), many=True
    )  # Accepts list of Food IDs

    class Meta:
        model = Meal
        fields = [
            "id",
            # "user",
            "date",
            "time",
            "food_info",
        ]  # You can also specify fields explicitly if needed

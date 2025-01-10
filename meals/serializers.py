from foods.models import Food
from meals.models import Meal
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


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


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        # Get the token object
        token = super().get_token(user)

        # Add custom claims to the token payload
        token["username"] = user.username
        token["is_admin"] = (
            user.is_staff
        )  # Assuming 'is_admin' corresponds to `is_staff`

        return token

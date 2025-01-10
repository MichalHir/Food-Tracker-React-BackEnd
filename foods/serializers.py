from foodTypes.serializers import FoodTypeSerializer
from foods.models import Food
from rest_framework import serializers


class FoodSerializer(serializers.ModelSerializer):
    types = FoodTypeSerializer(many=True, read_only=True)  # Nested serializer for types

    class Meta:
        model = Food
        fields = "__all__"  # or specify fields explicitly

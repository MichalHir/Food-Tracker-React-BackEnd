from rest_framework import serializers
from foodTypes.models import Food_type


class FoodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food_type
        fields = "__all__"  # or specify fields explicitly if needed

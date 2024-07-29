from rest_framework import serializers

from core.models import CustomUser, Car


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ["id", "username"]


class ListCarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = [
            'id', 'user', 'brand', 'model', 'version', 'year', 'mileage', 'displacement', 'power', 'fuel_type',
            'gearbox', 'propulsion', 'color', 'is_accident_free', 'condition', 'price',
        ]
        read_only_fields = ('id', 'user', 'price')


class CreateCarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = [
            'brand', 'model', 'version', 'year', 'mileage', 'displacement', 'power', 'fuel_type',
            'gearbox', 'propulsion', 'color', 'is_accident_free', 'condition',
        ]

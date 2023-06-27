from rest_framework import serializers
from .models import Car


class CarModelSerilizers(serializers.ModelSerializer):
    class Meta:
        model=Car
        fields='__all__'
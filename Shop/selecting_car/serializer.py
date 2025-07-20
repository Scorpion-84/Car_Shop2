from rest_framework import serializers
from .models import SelectCar

class SelectCarSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = SelectCar
        fields = '__all__'
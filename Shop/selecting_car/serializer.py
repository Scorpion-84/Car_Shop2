from rest_framework import serializers
from .models import SelectCar
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class SelectCarSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = SelectCar
        fields = '__all__'
        
class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, min_length = 8)
    
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password']
        
        def validate(self, data):
            
            if get_user_model().objects.filter(email = data.get('email')).exists():
                raise serializers.ValidationError({'email': 'This email is already in use.'})
            return data
        
        def create(self, validated_data):
            user = get_user_model().objects.create_user(
                username = validated_data['username'],
                email = validated_data.get('email', ''),
                password = validated_data['password']
            )
            return user                
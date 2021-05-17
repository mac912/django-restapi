from rest_framework import serializers
from .models import EmployeDetails

class EmployeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    email = serializers.EmailField()
    employid = serializers.CharField(max_length=10)
    phone = serializers.CharField(max_length=10)

    def create(self, validated_data):
        print("create method called")
        return EmployeDetails.objects.create(**validated_data)

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    email = serializers.EmailField()
    password = serializers.CharField()
    

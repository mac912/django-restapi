from rest_framework import serializers
from .models import EmployeDetails

class EmployeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    email = serializers.EmailField()
    employid = serializers.CharField(max_length=10)
    phone = serializers.CharField(max_length=10)

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    email = serializers.EmailField()
    password = serializers.CharField()
    

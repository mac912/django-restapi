from rest_framework import serializers
from .models import EmployeDetails
from django.contrib.auth.models import User

class EmployeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeDetails
        fields='__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    

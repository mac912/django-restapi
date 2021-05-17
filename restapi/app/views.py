from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
# Create your views here.
from .models import EmployeDetails
from .serializers import EmployeSerializer, UserSerializer
from django.contrib.auth.models import User

def index(request):
    employobj = EmployeDetails.objects.all()
    serializer = EmployeSerializer(employobj, many=True)
    return JsonResponse(serializer.data, safe=False)

def UserListView(request):
    Userobj = User.objects.all()
    serializers = UserSerializer(Userobj, many=True)
    return JsonResponse(serializers.data, safe=False)



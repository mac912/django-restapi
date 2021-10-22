#from django.shortcuts import render, HttpResponse
#from django.http import JsonResponse
# Create your views here.
from .models import EmployeDetails
from .serializers import EmployeSerializer, UserSerializer
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
#from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        employobj = EmployeDetails.objects.all()
        serializer = EmployeSerializer(employobj, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EmployeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        #return JsonResponse({"Message":"Add Employee"}, safe=False)

@api_view(['GET'])
def UserListView(request):
    Userobj = User.objects.all()
    serializers = UserSerializer(Userobj, many=True)
    return Response(serializers.data)

@api_view(['GET', 'DELETE', 'PUT'])
def EmployeeDetailView(request, pk):
    try:
        employee = EmployeDetails.objects.get(pk=pk)
    except EmployeDetails.DoesNotExist:
        return Response(status=404)

    if request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'GET':
        serializer = EmployeSerializer(employee)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EmployeSerializer(employee, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)




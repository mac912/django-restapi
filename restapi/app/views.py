from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
# Create your views here.
from .models import EmployeDetails
from .serializers import EmployeSerializer, UserSerializer
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

@csrf_exempt
def index(request):
    if request.method == 'GET':
        employobj = EmployeDetails.objects.all()
        serializer = EmployeSerializer(employobj, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        jsonData = JSONParser().parse(request)
        print(jsonData)
        serializer = EmployeSerializer(data = jsonData)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(serializer.errors, safe=False)
        #return JsonResponse({"Message":"Add Employee"}, safe=False)

def UserListView(request):
    Userobj = User.objects.all()
    serializers = UserSerializer(Userobj, many=True)
    return JsonResponse(serializers.data, safe=False)



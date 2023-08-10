from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Department
from django.views.decorators.csrf import csrf_exempt
from UserManagement.serializer import DepartmentSerializer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
@api_view(['GET','POST'])
def index(request):
    if request.method == "GET":
        avalvacancy = Department.objects.all()
        serializer = DepartmentSerializer(avalvacancy, many=True)
        # print(serializer)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    return  HttpResponse("Home")




@api_view(['DELETE', 'PUT','GET'])
def usersdetails(request,pk):
    try:
         vacancyID = Department.objects.get(pk=pk)
         
    except Department.DoesNotExist:
        return HttpResponse("User Does not exit")
   
    if request.method == "DELETE":
        vacancyID.delete()        
        return Response(vacancyID.title + "Deleted")
    elif request.method == "GET":
        serializer = DepartmentSerializer(vacancyID)
        return Response(serializer.data)
        
    elif request.method == "PUT":
        jsonData = JSONParser().parse(request)
        serializer = DepartmentSerializer(vacancyID, data=jsonData)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


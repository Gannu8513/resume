from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import User
from UserManagement.serializer import UserSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
@api_view(['GET','POST'])
def index(request):
    if request.method == "GET":
        avalvacancy = User.objects.all()
        serializer = UserSerializer(avalvacancy, many=True)
        # print(serializer)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    return  HttpResponse("Home")




@api_view(['DELETE', 'PUT','GET'])
def usersdetails(request,pk):
    try:
         vacancyID = User.objects.get(pk=pk)
         
    except User.DoesNotExist:
        return HttpResponse("User Does not exit")
   
    if request.method == "DELETE":
        vacancyID.delete()        
        return Response(vacancyID.title + "Deleted")
    elif request.method == "GET":
        serializer = UserSerializer(vacancyID)
        return Response(serializer.data)
        
    elif request.method == "PUT":
        jsonData = JSONParser().parse(request)
        serializer = UserSerializer(vacancyID, data=jsonData)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


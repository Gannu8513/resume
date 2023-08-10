from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Agency
from UserManagement.serializer import AgencySerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
@api_view(['GET','POST'])
def index(request):
    if request.method == "GET":
        avalvacancy = Agency.objects.all()
        serializer = AgencySerializer(avalvacancy, many=True)
        # print(serializer)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = AgencySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    return  HttpResponse("Home")




@api_view(['DELETE', 'PUT','GET'])
def usersdetails(request,pk):
    try:
         agencyID = Agency.objects.get(pk=pk)
         print(agencyID)
         
    except Agency.DoesNotExist:
        return HttpResponse("User Does not exit")
        print("Data Not Available")
   
    if request.method == "DELETE":
        agencyID.delete()        
        return Response(agencyID.title + "Deleted")
    elif request.method == "GET":
        serializer = AgencySerializer(agencyID)
        return Response(serializer.data)
        
    elif request.method == "PUT":
        jsonData = JSONParser().parse(request)
        serializer = AgencySerializer(agencyID, data=jsonData)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


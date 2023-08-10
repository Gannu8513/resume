from rest_framework import serializers

from agenciesdetails.models import Agency
from departmentdetails.models import Department
from userdetails.models import User

class AgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Agency
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class  UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =  User
        fields = '__all__'

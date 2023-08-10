from django.db import models
from departmentdetails.models import Department
from agenciesdetails.models import Agency
# Create your models here.
class User(models.Model):
    Employee_Id = models.IntegerField()
    CID = models.IntegerField()
    name = models.CharField(max_length=1024)
    DOB = models.DateField(max_length=50)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    Agency_Name = models.ForeignKey(Agency, on_delete=models.CASCADE)
    Department_Name = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    # def select_valid_department(self):
    #     agency_id = Agency.objects.get(id)
    #     if self.agency_id:
    #         available_departments = Department.objects.filter(agency_id=self.agency_id)
    #         if self.department_id not in available_departments.values_list('id', flat=True):
    #             return None
    #     return self.department
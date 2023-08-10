from django.db import models
from agenciesdetails.models import Agency
# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=1024)
    Agency_Name = models.ForeignKey(Agency, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name
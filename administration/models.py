from django.db import models
from django.contrib.auth.models import User
class Employee(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,blank=False,null=False)
    DESIGNATIONS = (
        ('account','Account'),
    )
    name = models.CharField(max_length=50,blank=False,null=False)
    mobile = models.CharField(max_length=50,blank=False,null=False)
    designation = models.CharField(max_length=50,choices=DESIGNATIONS,blank=False,null=False)

    def __str__(self):
        return self.name
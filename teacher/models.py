from django.db import models

class TeacherInfo(models.Model):
    name = models.CharField(max_length=50,blank=False,null=False,unique=True)
    gender_choice = (
        ('male','Male'),
        ('female','Female')
    )
    gender = models.CharField(choices=gender_choice,max_length=6,blank=False,null=False)
    phone_number = models.CharField(max_length=15,blank=False,null=False)
    destination = models.CharField(max_length=50,blank=False,null=False)

    def __str__(self):
        return self.name
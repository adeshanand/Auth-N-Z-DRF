from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    contact = models.TextField()
    creator = models.ForeignKey(User,blank=False,null=False,on_delete=models.CASCADE)

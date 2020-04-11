from django.db import models

class RegistrationModel(models.Model):
    idno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    dept = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    contact = models.IntegerField(unique=True)
    password = models.CharField(max_length=30)
    designation = models.CharField(max_length=30,default=False)
    date_join = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30,default=False)
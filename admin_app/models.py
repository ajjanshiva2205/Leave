from django.db import models

class ApplyLeaveModel(models.Model):
    idno = models.IntegerField(primary_key=True)
    des = models.CharField(max_length=20)
    dept = models.CharField(max_length=20)
    gmail = models.EmailField()
    l_type = models.CharField(max_length=60)
    s_date = models.DateField()
    l_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=20,default=False)

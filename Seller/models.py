from django.db import models
from Guest.models import *
from Admin.models import *
# Create your models here.

class tbl_work(models.Model):
    name=models.CharField(max_length=50)
    rate=models.CharField(max_length=50)
    details=models.CharField(max_length=50)
    image=models.FileField(upload_to="MemberDocs/")
    video=models.FileField(upload_to="MemberDocs")
    seller=models.ForeignKey(tbl_seller,on_delete=models.CASCADE)
    worktype=models.ForeignKey(tbl_worktype,on_delete=models.CASCADE)

class tbl_wgallery(models.Model):
    image=models.FileField(upload_to="MemberDocs/")
    work=models.ForeignKey(tbl_work,on_delete=models.CASCADE)

class tbl_material(models.Model):
    name=models.CharField(max_length=50)
    image=models.FileField(upload_to="MemberDocs/")
    rate=models.CharField(max_length=50)
    stock=models.IntegerField()
    work=models.ForeignKey(tbl_work,on_delete=models.CASCADE)
    description=models.TextField()



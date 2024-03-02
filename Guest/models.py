from django.db import models
from Admin.models import tbl_location,tbl_district,tbl_place

# Create your models here.

class tbl_user(models.Model):
    name=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    address=models.TextField(max_length=50)
    location=models.ForeignKey(tbl_location,on_delete=models.CASCADE) 
    gender=models.CharField(max_length=50)
    photo=models.FileField(upload_to="MemberDocs/")
    password=models.CharField(max_length=50)

class tbl_seller(models.Model):
    name=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    address=models.TextField(max_length=50)
    gender=models.CharField(max_length=50)
    photo=models.FileField(upload_to="MemberDocs/")
    password=models.CharField(max_length=50)
    proof=models.FileField(upload_to="MemberDocs/")
    status=models.IntegerField(default=0)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)

class tbl_adminlogin(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
            
    

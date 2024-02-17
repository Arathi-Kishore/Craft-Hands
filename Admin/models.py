from django.db import models

# Create your models here.
class tbl_worktype (models.Model):
    worktype=models.CharField(max_length=50)

class tbl_district (models.Model):
    district_name=models.CharField(max_length=50)

class tbl_place (models.Model):
    place_name=models.CharField(max_length=50)
    latitude=models.CharField(max_length=50)  
    longitude=models.CharField(max_length=50) 
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)

class tbl_location (models.Model):   
    name=models.CharField(max_length=50)
    latitude=models.CharField(max_length=50)  
    longitude=models.CharField(max_length=50)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE) 



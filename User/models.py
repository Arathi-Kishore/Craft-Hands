from django.db import models
from Guest.models import *
from Seller.models import *
# Create your models here.
class tbl_wbooking(models.Model):
    status=models.IntegerField(default=0)
    date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE) 

class tbl_wcart(models.Model):
    qty=models.IntegerField(default=1)
    cstatus=models.IntegerField(default=0)
    works=models.ForeignKey(tbl_work,on_delete=models.CASCADE) 
    wbooking=models.ForeignKey(tbl_wbooking,on_delete=models.CASCADE) 

class tbl_mbooking(models.Model):
    status=models.IntegerField(default=0)
    date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)

class tbl_mcart(models.Model):
    qty=models.IntegerField(default=1)
    cstatus=models.IntegerField(default=0)
    material=models.ForeignKey(tbl_material,on_delete=models.CASCADE)
    mbooking=models.ForeignKey(tbl_mbooking,on_delete=models.CASCADE) 

class Chat(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    from_user = models.ForeignKey(
        tbl_user, on_delete=models.SET_NULL, default=False, null=True, related_name="from_user")
    to_user = models.ForeignKey(
        tbl_user, on_delete=models.SET_NULL, default=False, null=True, related_name="to_user")
    from_seller = models.ForeignKey(
        tbl_seller, on_delete=models.SET_NULL, default=False, null=True, related_name="from_seller")
    to_seller = models.ForeignKey(
        tbl_seller, on_delete=models.SET_NULL, default=False, null=True, related_name="to_seller")
    content = models.TextField()






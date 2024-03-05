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


class tbl_star(models.Model):
    rating_data=models.IntegerField()
    user_name=models.CharField(max_length=50)
    user_review=models.CharField(max_length=50)
    datetime=models.DateField(auto_now_add=True)
    work_id=models.ForeignKey(tbl_work,on_delete=models.CASCADE)

class tbl_videopay(models.Model):
    seller=models.ForeignKey(tbl_seller,on_delete=models.CASCADE)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE) 

class tbl_complaint(models.Model):
    title=models.CharField(max_length=50) 
    content=models.CharField(max_length=50)
    status=models.IntegerField(default=0) 
    reply=models.CharField(max_length=50)
    reply_date=models.DateField(auto_now_add=True)
    date = models.DateTimeField(auto_now_add=True)
    seller=models.ForeignKey(tbl_seller,on_delete=models.SET_NULL,null=True)
    user=models.ForeignKey(tbl_user,on_delete=models.SET_NULL,null=True)     





class tbl_return(models.Model):
    cart=models.ForeignKey(tbl_mcart,on_delete=models.SET_NULL,null=True)
    reason=models.CharField(max_length=100)
    wcart=models.ForeignKey(tbl_wcart,on_delete=models.SET_NULL,null=True)
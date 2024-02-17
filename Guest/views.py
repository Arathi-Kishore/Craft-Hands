from django.shortcuts import render,redirect
from .models import *
from Admin.models import *

# Create your views here.
def user(request):
    disdata=tbl_district.objects.all()
    if request.method=="POST":
        loc=tbl_location.objects.get(id=request.POST.get('select_location'))
        tbl_user.objects.create(name=request.POST.get("txt_name"),contact=request.POST.get("txt_con"),email=request.POST.get("txt_email"),address=request.POST.get("txt_add"),location=loc,gender=request.POST.get("btn_gen"),photo=request.FILES.get('txt_pic'),password=request.POST.get("txt_pass"))
        return render(request,"Guest/UserRegistration.html",{'disdata':disdata})
    else:
        return render(request,"Guest/UserRegistration.html",{'disdata':disdata})
  

def login(request):
    if request.method=="POST":
        Email=request.POST.get('txt_email')
        Password=request.POST.get('txt_pass')

        ucount=tbl_user.objects.filter(email=Email,password=Password).count()
        scount=tbl_seller.objects.filter(email=Email,password=Password,status=1).count()
        if ucount > 0:
            userdata=tbl_user.objects.get(email=Email,password=Password)
            request.session['uid']=userdata.id
            return redirect('User:UserHome')
        elif scount > 0:
            sellerdata=tbl_seller.objects.get(email=Email,password=Password)
            request.session['sid']=sellerdata.id
            return redirect('Seller:SellerHome')    
        else:
            msg = "Invalid Credentials!!"
            return render(request,"Guest/Login.html",{'msg':msg})
    else:
        return render(request,"Guest/Login.html")    


def ajaxlocation(request):
    placedata=tbl_place.objects.get(id=request.GET.get('place'))
    locdata=tbl_location.objects.filter(place=placedata)
    return render(request,"Guest/AjaxLocation.html",{'data':locdata})

def seller(request):
    disdata=tbl_district.objects.all()
    if request.method=="POST":
        loc=tbl_place.objects.get(id=request.POST.get('select_place'))
        tbl_seller.objects.create(name=request.POST.get("txt_name"),contact=request.POST.get("txt_con"),email=request.POST.get("txt_email"),address=request.POST.get("txt_add"),gender=request.POST.get("btn_gen"),photo=request.FILES.get('txt_pic'),password=request.POST.get("txt_pass"),proof=request.FILES.get("txt_proof"),place=loc)
        return render(request,"Guest/SellerRegistration.html",{'disdata':disdata})
    else:
        return render(request,"Guest/SellerRegistration.html",{'disdata':disdata})
        
def index(request):
    return render(request,"Guest/index.html")
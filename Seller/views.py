from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from Seller.models import *
# Create your views here.

def sellerhome(request):
    sdata=tbl_seller.objects.get(id=request.session['sid'])
    return render(request,"Seller/SellerHome.html",{'sdata':sdata}) 

def myprofile(request):
    sdata=tbl_seller.objects.get(id=request.session['sid'])
    return render(request,"Seller/MyProfile.html",{'sdata':sdata})

def editprof(request):
    sdata=tbl_seller.objects.get(id=request.session['sid'])
    if request.method=="POST":
        sdata.name=request.POST.get("txt_name")
        sdata.contact=request.POST.get("txt_con")
        sdata.email=request.POST.get("txt_email")
        sdata.address=request.POST.get("txt_address")
        sdata.save()
        return redirect("Seller:MyProfile")
    else:
        return render(request,"Seller/EditProfile.html",{'sdata':sdata})

def changepass(request):
    sdata=tbl_seller.objects.get(id=request.session['sid'])
    if request.method=="POST":
        pwd=sdata.password
        current_pwd=request.POST.get("txt_pass")
        if pwd == current_pwd:
            pass1=request.POST.get("txt_new")
            pass2=request.POST.get("txt_cpass")
            if pass1==pass2 :
                sdata.password=pass1
                sdata.save()
                return redirect("Seller:ChangePassword")
            else:
                msg="password does not match"
                return render("Seller/ChangePassword.html",{'msg':msg})
        else:
            msg="incorrect password"
            return render("Seller/ChangePassword.html",{'msg':msg})
    else:
        msg="password changed"
        return render(request,"Seller/ChangePassword.html",{'msg':msg})        

def addwork(request):
    sdata=tbl_seller.objects.get(id=request.session['sid'])
    worktypedata=tbl_worktype.objects.all()
    workdata=tbl_work.objects.filter(seller=sdata)
    if request.method=="POST":
        wdata=tbl_worktype.objects.get(id=request.POST.get('select_work'))
        tbl_work.objects.create(worktype=wdata,name=request.POST.get('txt_name'),rate=request.POST.get('txt_rate'),details=request.POST.get('txt_det'),image=request.FILES.get('txt_pic'),video=request.FILES.get('txt_vid'),seller=sdata)
        return render(request,"Seller/AddWork.html",{'worktypedata':worktypedata,'workdata':workdata})
    else:    
        return render(request,"Seller/AddWork.html",{'worktypedata':worktypedata,'workdata':workdata})

def addmat(request,wid):
    wdata=tbl_work.objects.get(id=wid)
    materialdata=tbl_material.objects.all()
    if request.method=="POST":
        tbl_material.objects.create(name=request.POST.get('txt_name'),rate=request.POST.get('txt_rate'),description=request.POST.get('txt_des'),image=request.FILES.get('txt_pic'),stock=request.POST.get('txt_stock'),work=wdata)
        return render(request,"Seller/AddMaterial.html",{'wdata':wdata})
    else:
        return render(request,"Seller/AddMaterial.html",{'wdata':wdata})   

def DeleteMaterial(request,did):
    tbl_material.objects.get(id=did).delete()
    return redirect("Seller:AddMaterial") 


def wgall(request,wid):
    if request.method=="POST" and request.FILES:
        wdata=tbl_work.objects.get(id=wid)
        tbl_wgallery.objects.create(work=wdata,image=request.FILES.get("txt_img"))
        return render(request,"Seller/WorkGallery.html") 
    else:
        return render(request,"Seller/WorkGallery.html")

def DeleteWork(request,did):
    tbl_work.objects.get(id=did).delete()
    return redirect("Seller:AddWork") 



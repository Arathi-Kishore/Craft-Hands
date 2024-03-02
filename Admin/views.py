from django.shortcuts import render,redirect
from .models import *
from Guest.models import *
# Create your views here.

def dis(request):
    disdata=tbl_district.objects.all()
    if request.method=="POST":
        datacount= tbl_district.objects.filter(district_name=request.POST.get("txt_district")).count()
        if datacount>0:
            return render(request,"Admin/District.html",{'district':disdata}) 
        else:      
            tbl_district.objects.create(district_name=request.POST.get("txt_district"))
            return render(request,"Admin/District.html",{'district':disdata})
    else:
        return render(request,"Admin/District.html",{'district':disdata})

def DeleteDistrict(request,did): 
    tbl_district.objects.get(id=did).delete()
    return redirect("Admin:District")

def EditDistrict(request,eid):
    dis=tbl_district.objects.get(id=eid)
    if request.method=="POST":
       dis.district_name=request.POST.get("txt_district")
       dis.save()
       return redirect("Admin:District")
    else:
        return render(request,"Admin/District.html",{'edis':dis})


def pla(request):
    disdata=tbl_district.objects.all()
    subdata=tbl_place.objects.all()
    if request.method=="POST":
        dis = tbl_district.objects.get(id=request.POST.get("select_dis"))
        datacount=tbl_place.objects.filter( place_name=request.POST.get("txt_place"), district=dis).count()
        if datacount>0:
            return render(request,"Admin/Place.html",{'disdata':disdata,'subcat':subdata})
        else:
                tbl_place.objects.create(
                place_name=request.POST.get("txt_place"),
                district=dis,longitude=request.POST.get('txt_longi'),latitude=request.POST.get('txt_lati')
        )
        return render(request,"Admin/Place.html",{'disdata':disdata,'subcat':subdata})
    else:    
        return render(request,"Admin/Place.html",{'disdata':disdata,'subcat':subdata})


def DeletePlace(request,did):
    tbl_place.objects.get(id=did).delete()
    return redirect("Admin:Place")

def ajaxplace(request):
    disdata=tbl_district.objects.get(id=request.GET.get('Dist'))
    place=tbl_place.objects.filter(district=disdata)
    return render(request,"Admin/Ajaxplace.html",{'pl':place})
def loc(request):
    disdata=tbl_district.objects.all()
    subdata=tbl_location.objects.all()
    if request.method=="POST":
        dis = tbl_place.objects.get(id=request.POST.get("select_place"))
        datacount= tbl_location.objects.filter(name=request.POST.get("txt_location"),
        place=dis).count()
        if datacount>0:
                return render(request,"Admin/Location.html",{'disdata':disdata,'loc':subdata})
        else:
                tbl_location.objects.create(
            name=request.POST.get("txt_location"),
            place=dis,
            latitude=request.POST.get("txt_lati"),
            longitude=request.POST.get("txt_longi")
        )
        return render(request,"Admin/Location.html",{'disdata':disdata,'loc':subdata})
    else:    
        return render(request,"Admin/Location.html",{'disdata':disdata,'loc':subdata})       

def Deletelocation(request,did):
    tbl_location.objects.get(id=did).delete()
    return redirect("Admin:Location")

def WorkType(request):
    disdata=tbl_worktype.objects.all()
    if request.method=="POST":
        datacount= tbl_worktype.objects.filter(worktype=request.POST.get("txt_work")).count()
        if datacount>0:
            return render(request,"Admin/WorkType.html",{"WorkType":disdata})
        else:
            tbl_worktype.objects.create(worktype=request.POST.get("txt_work"))
        return render(request,"Admin/WorkType.html",{"WorkType":disdata})
    else:
        return render(request,"Admin/WorkType.html",{'WorkType':disdata})
   
def DeleteWork(request,did):
    tbl_worktype.objects.get(id=did).delete()
    return redirect("Admin:WorkType")

def EditWork(request,eid):
    dis=tbl_worktype.objects.get(id=eid)
    if request.method=="POST":
       dis.worktype=request.POST.get("txt_work")
       dis.save()
       return redirect("Admin:WorkType")
    else:
        return render(request,"Admin/WorkType.html",{'edis':dis})

def sellerlist(request):
    selldata=tbl_seller.objects.filter(status=0)
    return render(request,"Admin/ViewSellerList.html",{'selldata':selldata})        

def acceptlist(request):
    selldata=tbl_seller.objects.filter(status=1)
    return render(request,"Admin/AcceptedList.html",{'selldata':selldata})  

def rejectlist(request):
    selldata=tbl_seller.objects.filter(status=2)
    return render(request,"Admin/RejectedList.html",{'selldata':selldata})  

def accept(request,aid):
    sellerdata=tbl_seller.objects.get(id=aid)
    sellerdata.status=1
    sellerdata.save()
    return redirect("Admin:ViewSellerList")

def reject(request,rid):
    sellerdata=tbl_seller.objects.get(id=rid)
    sellerdata.status=2
    sellerdata.save()
    return redirect("Admin:ViewSellerList")

def adminhome(request):
    return render(request,"Admin/AdminHome.html")        


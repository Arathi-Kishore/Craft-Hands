from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from Seller.models import *
from User.models import *
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

def userbooking(request):
    userdata=tbl_seller.objects.get(id=request.session['sid'])
    data=tbl_wcart.objects.filter(works__seller=userdata,wbooking__status=0)
    return render(request,"Seller/UserBooking.html",{'data':data})

def acceptlist(request):
    userdata=tbl_seller.objects.get(id=request.session['sid'])
    data=tbl_wcart.objects.filter(works__seller=userdata,wbooking__status=1)
    return render(request,"Seller/AcceptedList.html",{'selldata':data})

def rejectlist(request):
    userdata=tbl_seller.objects.get(id=request.session['sid'])
    data=tbl_wcart.objects.filter(works__seller=userdata,wbooking__status=2)
    return render(request,"Seller/RejectedList.html",{'selldata':data})

def accept(request,aid):
    sellerdata=tbl_wbooking.objects.get(id=aid)
    sellerdata.status=1
    sellerdata.save()
    return redirect("Seller:Userbooking")

def reject(request,rid):
    sellerdata=tbl_wbooking.objects.get(id=rid)
    sellerdata.status=2
    sellerdata.save()
    return redirect("Admin:Userbooking")    

def chatuser(request, cid):
    chatobj = tbl_wbooking.objects.get(id=cid)
    if request.method == "POST":
        cied = request.POST.get("cid")
        # print(cied)
        ciedobj = tbl_user.objects.get(id=cied)
        sobj = tbl_seller.objects.get(id=request.session["sid"])
        content = request.POST.get("msg")
        # print(cied)
        # print(content)
        Chat.objects.create(
            from_seller=sobj, to_user=ciedobj, content=content, from_user=None, to_seller=None)
        return render(request, 'Seller/Chat.html', {"chatobj": chatobj})
    else:
        return render(request, 'Seller/Chat.html', {"chatobj": chatobj})


def loadchatuser(request):
    cid = request.GET.get("cid")
    request.session["cid"] = cid

    cid1 = request.session["cid"]
    # print(cid1)

    # print(cid)
    shopobj = tbl_user.objects.get(id=cid)
    # print(userobj)
    sid = request.session["sid"]
    # print(sid)
    suserobj = tbl_seller.objects.get(id=request.session["sid"])
    # chatobj1 = Chat.objects.filter(Q(to_user=suserobj) | Q(
    #     from_user=suserobj), Q(to_shop=shopobj) | Q(from_shop=shopobj))
    # print(chatobj1)  # send message

    # print(chatobj2)  # recived msg
    chatobj = Chat.objects.raw(
        "select * from User_chat c inner join Guest_tbl_seller u on (u.id=c.from_seller_id) or (u.id=c.to_seller_id) WHERE  c.from_user_id=%s or c.to_user_id=%s order by c.date", params=[(cid1), (cid1)])

    print(chatobj.query)

    return render(request, 'Seller/Load.html', {"obj": chatobj, "sid": sid, "shop": shopobj, "userobj": suserobj})


def complaint(request):
    sdata=tbl_seller.objects.get(id=request.session['sid'])

    compdata=tbl_complaint.objects.all()
    if request.method=="POST":
        tbl_complaint.objects.create(    
            title = request.POST.get("txt_title"),
            content = request.POST.get("txt_content"),
            seller=sdata,

        )
        return render(request,"Seller/Complaint.html",{'sdata':sdata,'compdata':compdata}) 
    else:
        return render(request,"Seller/Complaint.html",{'sdata':sdata,'compdata':compdata})

def DeleteComplaint(request,did):
    tbl_complaint.objects.get(id=did).delete()
    return redirect("Seller:complaint")        

  

    



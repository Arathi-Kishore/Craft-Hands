from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from Seller.models import *
from datetime import datetime,timedelta
from User.models import tbl_wcart,tbl_mcart
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
    materialdata=tbl_material.objects.filter(work=wdata)
    if request.method=="POST":
        tbl_material.objects.create(name=request.POST.get('txt_name'),rate=request.POST.get('txt_rate'),description=request.POST.get('txt_des'),image=request.FILES.get('txt_pic'),stock=request.POST.get('txt_stock'),work=wdata)
        return render(request,"Seller/AddMaterial.html",{'wdata':wdata,'mdata':materialdata})
    else:
        return render(request,"Seller/AddMaterial.html",{'wdata':wdata,'mdata':materialdata})   

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

# def userbooking(request):
#     userdata=tbl_seller.objects.get(id=request.session['sid'])
#     data=tbl_wcart.objects.filter(works__seller=userdata,wbooking__status=0)
#     return render(request,"Seller/UserBooking.html",{'data':data})

# def acceptlist(request):
#     userdata=tbl_seller.objects.get(id=request.session['sid'])
#     data=tbl_wcart.objects.filter(works__seller=userdata,wbooking__status=1)
#     return render(request,"Seller/AcceptedList.html",{'selldata':data})

# def rejectlist(request):
#     userdata=tbl_seller.objects.get(id=request.session['sid'])
#     data=tbl_wcart.objects.filter(works__seller=userdata,wbooking__status=2)
#     return render(request,"Seller/RejectedList.html",{'selldata':data})

# def accept(request,aid):
#     sellerdata=tbl_wbooking.objects.get(id=aid)
#     sellerdata.status=1
#     sellerdata.save()
#     return redirect("Seller:Userbooking")

# def reject(request,rid):
#     sellerdata=tbl_wbooking.objects.get(id=rid)
#     sellerdata.status=2
#     sellerdata.save()
#     return redirect("Seller:Userbooking")    

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

  
def logout(request):
    del request.session["sid"]
    return redirect("Guest:login")
    


def itempacked(request,pid):
    data=tbl_wcart.objects.get(id=pid)
    data.cstatus=5
    data.save()
    return redirect("Seller:Userbooking")
def itemshipped(request,shid):
    data=tbl_wcart.objects.get(id=shid)
    data.cstatus=6
    data.save()
    return redirect("Seller:Userbooking")
def itemdispatched(request,did):
    data=tbl_wcart.objects.get(id=did)
    data.cstatus=7
    data.save()
    return redirect("Seller:Userbooking")
def delivered(request,ddid):
    data=tbl_wcart.objects.get(id=ddid)
    data.cstatus=8
    data.save()
    return redirect("Seller:Userbooking")
# material
def mitempacked(request,pid):
    data=tbl_mcart.objects.get(id=pid)
    data.cstatus=2
    data.save()
    return redirect("Seller:materialbooking")
def mitemshipped(request,shid):
    data=tbl_mcart.objects.get(id=shid)
    data.cstatus=3
    data.save()
    return redirect("Seller:materialbooking")
def mitemdispatched(request,did):
    data=tbl_mcart.objects.get(id=did)
    data.cstatus=4
    data.save()
    return redirect("Seller:materialbooking")
def mdelivered(request,ddid):
    data=tbl_mcart.objects.get(id=ddid)
    data.cstatus=5
    data.save()
    return redirect("Seller:materialbooking")

def workreport(request):
    if 'sid' in request.session:
        total=0
        slr=tbl_seller.objects.get(id=request.session["sid"])
    # mdata=tbl_wcart.objects.filter(works__seller=slr)
        if request.method == "POST":
            if request.POST.get('fdate')!="" and request.POST.get('edate')!="":
                data1=tbl_wcart.objects.filter(wbooking__date__gt=request.POST.get('fdate'),wbooking__date__lt=request.POST.get('edate'),works__seller=slr)
                for i in data1:
                    total=total+(int(i.qty)*int(i.works.rate))
                return render(request,"Seller/WorkBookingReport.html",{'data1':data1,'total':total})
            elif request.POST.get('fdate')!="" and request.POST.get('edate') =="":
                data2=tbl_wcart.objects.filter(wbooking__date__gt=request.POST.get('fdate'),works__seller=slr)
                for i in data2:
                    total=total+(int(i.qty)*int(i.works.rate))
                return render(request,"Seller/WorkBookingReport.html",{'data1':data2,'total':total})
            elif request.POST.get('fdate') =="" and request.POST.get('edate')!="":
                data3=tbl_wcart.objects.filter(wbooking__date__lt=request.POST.get('edate'),works__seller=slr)
                for i in data3:
                    total=total+(int(i.qty)*int(i.works.rate))
                return render(request,"Seller/WorkBookingReport.html",{'data1':data3,'total':total})
            else:
                return render(request,"Seller/WorkBookingReport.html")
        else:
                return render(request,"Seller/WorkBookingReport.html")
    else:
        return redirect("Guest:login")

def materialreport(request):
    if 'sid' in request.session:
        slr=tbl_seller.objects.get(id=request.session["sid"])
        #mdata=tbl_mcart.objects.filter(material__work__seller=slr)
        if request.method == "POST":
            if request.POST.get('fdate')!="" and request.POST.get('edate')!="":
                data1=tbl_mcart.objects.filter(mbooking__date__gt=request.POST.get('fdate'),mbooking__date__lt=request.POST.get('edate'),material__work__seller=slr)
                return render(request,"Seller/MaterialBookingReport.html",{'data':data1})
            elif request.POST.get('fdate')!="" and request.POST.get('edate') =="":
                data2=tbl_mcart.objects.filter(mbooking__date__gt=request.POST.get('fdate'),material__work__seller=slr)
                return render(request,"Seller/MaterialBookingReport.html",{'data':data2})
            elif request.POST.get('fdate') =="" and request.POST.get('edate')!="":
                data3=tbl_mcart.objects.filter(mbooking__date__lt=request.POST.get('edate'),material__work__seller=slr)
                return render(request,"Seller/MaterialBookingReport.html",{'data':data3})
            else:
                return render(request,"Seller/MaterialBookingReport.html")
        else:
            return render(request,"Seller/MaterialBookingReport.html")
    else:
        return redirect("Guest:login")

def viewreason(request,mid):
    data=tbl_mcart.objects.get(id=mid)
    rdata=tbl_return.objects.get(cart=data)
    return render(request,"Seller/ViewReason.html",{'data':rdata})
def verifyreason(request,rid):
    data=tbl_return.objects.get(id=rid)
    ddata=tbl_mcart.objects.get(id=data.cart.id)
    ddata.cstatus=8
    ddata.save()
    return redirect("Seller:Userbooking")
    #product return reason
def wviewreason(request,wid):
    data=tbl_wcart.objects.get(id=wid)
    rdata=tbl_return.objects.get(wcart=data)
    return render(request,"Seller/ViewReason.html",{'data':rdata,'ms':1})
def wverifyreason(request,pid):
    data=tbl_return.objects.get(id=pid)
    ddata=tbl_wcart.objects.get(id=data.wcart.id)
    
    ddata.cstatus=10
    ddata.save()
    return redirect("Seller:Userbooking")


def userbooking(request):

    if 'sid' in request.session:
        slr=tbl_seller.objects.get(id=request.session["sid"])
        data=tbl_wcart.objects.filter(works__seller=slr)
        return render(request,"Seller/Userbooking.html",{'data':data})
    else:
       return redirect("Guest:login")

def materialbooking(request):

    if 'sid' in request.session:
        slr=tbl_seller.objects.get(id=request.session["sid"])
        mdata=tbl_mcart.objects.filter(material__work__seller=slr)
        return render(request,"Seller/Materialbooking.html",{'data':mdata})
    else:
       return redirect("Guest:login")



def rejectorder(request,rid):
    data=tbl_mcart.objects.get(id=rid)
    bid=data.mbooking.id
    mbdata=tbl_mbooking.objects.get(id=bid)
    name=mbdata.user.name
    email=mbdata.user.email
    data.cstatus=9
    data.save()
    return redirect("Seller:Userbooking")

def rejectwork(request,rrid):
    
    data=tbl_wcart.objects.get(id=rrid)
    bdata=tbl_wbooking.objects.get(id=data.booking.id)
    name=bdata.user.name
    email=bdata.user.email
    data.cstatus=4
    data.save()
    return redirect("Seller:Userbooking")
    



def acceptorder(request,aid):
    data=tbl_mcart.objects.get(id=aid)
    bid=data.mbooking.id
    mbdata=tbl_mbooking.objects.get(id=bid)
    name=mbdata.user.name
    email=mbdata.user.email  
    data.cstatus=1
    data.save()
    return redirect("Seller:Userbooking")
   

def acceptwork(request,aaid):
    wdata=tbl_wcart.objects.get(id=aaid)
    bdata=tbl_wbooking.objects.get(id=wdata.wbooking.id)
    name=bdata.user.name
    email=bdata.user.email    
    wdata.cstatus=3
    wdata.save()
    return redirect("Seller:Userbooking")


def videoreport(request):
    sellerdata=tbl_seller.objects.get(id=request.session["sid"])
    data=tbl_videopay.objects.filter(seller=sellerdata)
    return render(request,"Seller/VideopaymentReport.html",{'data':data})

def weekly_booking_report(request):    # Get the current date
    current_date = datetime.now()    # Calculate the start date of the week (Sunday) and the end date of the week (Saturday)    
    slr=tbl_seller.objects.get(id=request.session["sid"])
    total=0
    start_of_week = current_date - timedelta(days=current_date.weekday())
    end_of_week = start_of_week + timedelta(days=6)    # Query the database for bookings within the current week   
    data1=tbl_wcart.objects.filter(booking__date__gt=start_of_week,booking__date__lt=end_of_week,works__seller=slr)
    for i in data1:
        total=total+(int(i.qty)*int(i.works.rate))
    return render(request,"Seller/WeeklyReport.html",{'data1':data1,'total':total})
   

def monthly_booking_report(request):    # Get the current date
    current_date = datetime.now()
    slr=tbl_seller.objects.get(id=request.session["sid"])
    total=0
    # Calculate the first day and the last day of the current month  
    first_day_of_month = current_date.replace(day=1)
    last_day_of_month = first_day_of_month.replace(month=first_day_of_month.month + 1, day=1) - timedelta(days=1)
    # Query the database for bookings within the current month 
    # monthly_bookings = Booking.objects.filter(booking_date__range=[first_day_of_month, last_day_of_month])
    # Calculate the count of bookings for each day in the month
    data1=tbl_wcart.objects.filter(booking__date__gt=first_day_of_month,booking__date__lt=last_day_of_month,works__seller=slr)
    for i in data1:
        total=total+(int(i.qty)*int(i.works.rate))
    return render(request,"Seller/MonthlyReport.html",{'data1':data1,'total':total}) 
    


def yearly_booking_report(request):    # Get the current date
    current_date = datetime.now()
    slr=tbl_seller.objects.get(id=request.session["sid"])
    total=0
    # Calculate the first day and the last day of the current year    
    first_day_of_year = current_date.replace(month=1, day=1)
    last_day_of_year = first_day_of_year.replace(year=first_day_of_year.year + 1) - timedelta(days=1)
    # Query the database for bookings within the current year  
    # yearly_bookings = Booking.objects.filter(booking_date__range=[first_day_of_year, last_day_of_year])
    # Calculate the count of bookings for each day in the year
    # daily_booking_count = yearly_bookings.annotate(date=models.functions.TruncDay('booking_date')).values('date').annotate(count=Count('id')).order_by('date')
    data1=tbl_wcart.objects.filter(booking__date__gt=first_day_of_year,booking__date__lt=last_day_of_year,works__seller=slr)
    for i in data1:
        total=total+(int(i.qty)*int(i.works.rate))
    return render(request,"Seller/YearlyReport.html",{'data1':data1,'total':total}) 

from django.shortcuts import render,redirect
from Guest.models import *
from Seller.models import *
from .models import *
from geopy.distance import geodesic
import random
import math
from datetime import date
# Create your views here.

def userhome(request):
    udata=tbl_user.objects.get(id=request.session['uid'])
    return render(request,"User/UserHome.html",{'udata':udata}) 

def myprofile(request):
    udata=tbl_user.objects.get(id=request.session['uid'])
    return render(request,"User/MyProfile.html",{'udata':udata})

def editprof(request):
    udata=tbl_user.objects.get(id=request.session['uid'])
    if request.method=="POST":
        udata.name=request.POST.get("txt_name")
        udata.contact=request.POST.get("txt_con")
        udata.email=request.POST.get("txt_email")
        udata.address=request.POST.get("txt_address")
        udata.save()
        return redirect("User:MyProfile")
    else:
        return render(request,"User/EditProfile.html",{'udata':udata})

def changepass(request):
    udata=tbl_user.objects.get(id=request.session['uid'])
    if request.method=="POST":
        pwd=udata.password
        current_pwd=request.POST.get("txt_pass")
        if pwd == current_pwd:
            pass1=request.POST.get("txt_new")
            pass2=request.POST.get("txt_cpass")
            if pass1==pass2 :
                udata.password=pass1
                udata.save()
                return redirect("User:ChangePassword")
            else:
                msg="password does not match"
                return render("User/ChangePassword.html",{'msg':msg})
        else:
            msg="incorrect password"
            return render("User/ChangePassword.html",{'msg':msg})
    else:
        msg="password changed"
        return render(request,"User/ChangePassword.html",{'msg':msg})        
                   

def viewwork(request,sid):
    sdata=tbl_seller.objects.get(id=sid)
    wdata=tbl_work.objects.filter(seller=sdata)
    rdata=tbl_seller.objects.all()
    return render(request,"User/ViewWorks.html",{'wdata':wdata,'rdata':rdata})

def viewworkmaterial(request,sid):
    sdata=tbl_work.objects.get(id=sid)
    wdata=tbl_material.objects.filter(work=sdata)
    return render(request,"User/ViewMaterial.html",{'wdata':wdata})

def searchsell(request):
    disdata=tbl_district.objects.all()
    subdata=tbl_place.objects.all()
    rdata=tbl_seller.objects.all()
    if request.method=="POST":
        return render(request,"User/SearchSeller.html",{'rdata': rdata, 'disdata':disdata,'subdata':subdata}) 
    else:   
        return render(request,"User/SearchSeller.html",{'rdata':rdata,'disdata':disdata,'subdata':subdata})

def addtocart(request,wid):
    userdata=tbl_user.objects.get(id=request.session['uid'])
    workdata=tbl_work.objects.get(id=wid)
    bcount=tbl_wbooking.objects.filter(user=userdata,status=0).count()
    if bcount>0:
        bookingdata=tbl_wbooking.objects.get(user=userdata,status=0)
        ccount=tbl_wcart.objects.filter(wbooking=bookingdata,works=workdata).count()
        if ccount>0:
            print("Already in Cart")
            return redirect("User:SearchSeller")
        else:
            tbl_wcart.objects.create(works=workdata,wbooking=bookingdata)
            return redirect("User:SearchSeller")
    else:
        tbl_wbooking.objects.create(user=userdata)
        bcount=tbl_wbooking.objects.filter(user=userdata,status=0).count()
        if bcount>0:
            bookingdata=tbl_wbooking.objects.get(user=userdata,status=0)
            ccount=tbl_wcart.objects.filter(wbooking=bookingdata,works=workdata).count()
            if ccount>0:
                print("Already in Cart")
                return redirect("User:SearchSeller")
            else:
                tbl_wcart.objects.create(works=workdata,wbooking=bookingdata)
                return redirect("User:SearchSeller")        


# def mycart(request):
#     userdata=tbl_user.objects.get(id=request.session['uid'])
#     cartdata=tbl_wcart.objects.filter(wbooking__user=userdata)
#     return render(request,"User/MyCart.html",{'userdata':userdata,'cartdata':cartdata})      


def addtocartmaterial(request,mid):
    userdata=tbl_user.objects.get(id=request.session['uid'])
    materialdata=tbl_material.objects.get(id=mid)
    bcount=tbl_mbooking.objects.filter(user=userdata,status=0).count()
    if bcount>0:
        bookingdata=tbl_mbooking.objects.get(user=userdata,status=0)
        ccount=tbl_mcart.objects.filter(mbooking=bookingdata,material=materialdata).count()
        if ccount>0:
            print("Already in Cart")
            return redirect("User:SearchSeller")
        else:
            tbl_mcart.objects.create(material=materialdata,mbooking=bookingdata)
            return redirect("User:SearchSeller")
    else:
        tbl_mbooking.objects.create(user=userdata)
        bcount=tbl_mbooking.objects.filter(user=userdata,status=0).count()
        if bcount>0:
            bookingdata=tbl_mbooking.objects.get(user=userdata,status=0)
            ccount=tbl_mcart.objects.filter(mbooking=bookingdata,material=materialdata).count()
            if ccount>0:
                print("Already in Cart")
                return redirect("User:SearchSeller")
            else:
                tbl_mcart.objects.create(material=materialdata,mbooking=bookingdata)
                return redirect("User:SearchSeller")  

def calculate_distance(lat1, lon1, lat2, lon2):
    # Using geopy's geodesic method to calculate the distance
    # 'geodesic' calculates the shortest path between two points on the surface of a spheroid (e.g., the Earth)
    coords1 = (lat1, lon1)
    coords2 = (lat2, lon2)
    distance_km = geodesic(coords1, coords2).kilometers
    return distance_km




def mycart(request):
    dist=[]
    if 'uid' in request.session:
        userdata=tbl_user.objects.get(id=request.session["uid"])
        lid=userdata.location.id
        ldata=tbl_location.objects.get(id=lid)
        lat1=ldata.latitude
        lonti=ldata.longitude    
        if request.method=="POST":
            return redirect("User:payment")
        else:
            shoparray=[]
            bcount=tbl_wbooking.objects.filter(user=userdata,status=0).count()
            mcount=tbl_mbooking.objects.filter(user=userdata,status=0).count()
            if bcount and mcount>0:
                bookdata=tbl_wbooking.objects.get(user=userdata,status=0)
                mbookdata=tbl_mbooking.objects.get(user=userdata,status=0)
                request.session["bookings"]=bookdata.id
                request.session["mbookings"]=mbookdata.id
                data=tbl_wcart.objects.filter(wbooking=bookdata)
                mdata=tbl_mcart.objects.filter(mbooking=mbookdata)
                for i in data:
                    shoparray.append(i.works.seller.id)
                for i in mdata:
                    shoparray.append(i.material.work.seller.id)
            #print(shoparray)
                for j in  shoparray:
                    shopdata=tbl_seller.objects.get(id=j)
                    l1id=shopdata.place.id
                    l2data=tbl_place.objects.get(id=l1id)
                    lat2=l2data.latitude
                    lon2=l2data.longitude
                    dt=calculate_distance(lat1, lonti, lat2, lon2)
                    dist.append(dt)
                #print(len(dist))
                if len(dist)>0:
                    highest=max(dist)
            
                    fraction,intpart=math.modf(highest)
                    fraction=fraction*1000
                    fraction=int(fraction)
                    message="Our Agent Will Traveling "+str(intpart)+"Kilometer"+"and "+str(fraction)+"Meters.."+"To Deliver Your Order"
                    request.session["mess"]=message
                return render(request,"User/MyCart.html",{'data':data,'data1':mdata})
            elif bcount>0:
                bookdata=tbl_wbooking.objects.get(user=userdata,status=0)
                request.session["bookings"]=bookdata.id
                data=tbl_wcart.objects.filter(wbooking=bookdata)
                for i in data:
                    shoparray.append(i.works.seller.id)
                
            #print(shoparray)
                for j in  shoparray:
                    shopdata=tbl_seller.objects.get(id=j)
                    l1id=shopdata.place.id
                    l2data=tbl_place.objects.get(id=l1id)
                    lat2=l2data.latitude
                    lon2=l2data.longitude
                    dt=calculate_distance(lat1, lonti, lat2, lon2)
                    dist.append(dt)
            #print(dist)
                if len(dist)>0:
                    highest=max(dist)
            
                    fraction,intpart=math.modf(highest)
                    fraction=fraction*1000
                    fraction=int(fraction)
                    message="Our Agent Will Traveling "+str(intpart)+"Kilometer"+"and "+str(fraction)+"Meters.."+"To Deliver Your Order"
                    request.session["mess"]=message
                return render(request,"User/MyCart.html",{'data':data})
            elif mcount>0:
                mbookdata=tbl_mbooking.objects.get(user=userdata,status=0)
                mdata=tbl_mcart.objects.filter(mbooking=mbookdata)
                for i in mdata:
                    shoparray.append(i.material.work.seller.id)
            #print(shoparray)
                for j in  shoparray:
                    shopdata=tbl_seller.objects.get(id=j)
                    l1id=shopdata.place.id
                    l2data=tbl_place.objects.get(id=l1id)
                    lat2=l2data.latitude
                    lon2=l2data.longitude
                    dt=calculate_distance(lat1, lonti, lat2, lon2)
                    dist.append(dt)
            #print(dist)
                highest=max(dist)
            
                fraction,intpart=math.modf(highest)
                fraction=fraction*1000
                fraction=int(fraction)
                message="Our Agent Will Traveling "+str(intpart)+"Kilometer"+"and "+str(fraction)+"To Deliver Your Order"
                request.session["mess"]=message
                request.session["mbookings"]=mbookdata.id
                mdata=tbl_mcart.objects.filter(mbooking=mbookdata)
                return render(request,"User/MyCart.html",{'data1':mdata})
            else:
                return render(request,"User/MyCart.html") 
    else:        
        return redirect("Guest:login")




def get_qnty(request):
    if 'uid' in request.session:

        qty=request.GET.get('QTY')
        alt=request.GET.get('ALT')
        cart=tbl_wcart.objects.get(id=alt)
        cart.qty=qty
        cart.save()
        return redirect('User:mycart')
    else:
        return redirect("Guest:login")

def get_qnty1(request):
    if 'uid' in request.session:

        qty=int(request.GET.get('QTY'))
        alt=request.GET.get('ALT')
        cart=tbl_mcart.objects.get(id=alt)
        productid=cart.material.id
        mdata=tbl_material.objects.get(id=productid)
        stock=int(mdata.stock)
        if qty>stock:

            cart.qty=stock
            cart.save()
            return redirect('User:mycart')
        else:
            cart.qty=qty
            cart.save()
            return redirect('User:mycart')
    else:
        return redirect("Guest:login")
def PAYMENT(request):   
    if 'uid' in request.session:
        if request.method=="POST": 
            #print(request.session["bookings"])
            if 'bookings'  in request.session and 'mbookings' in request.session:
                #print("hai")
                if request.session["bookings"]!="":
                    ids=tbl_wbooking.objects.get(id=request.session["bookings"])
                    ids.status=1
                    ids.save()
                if request.session["mbookings"]!="":
                    mdata=tbl_mbooking.objects.get(id=request.session["mbookings"])
                    mcartdatacount=tbl_mcart.objects.filter(mbooking=mdata).count()
                    if mcartdatacount>0:
                        mcartdata=tbl_mcart.objects.filter(mbooking=mdata)
                        for i in mcartdata:
                            mtdata=tbl_material.objects.get(id=i.material.id)
                            stock=int(mtdata.stock)
                            newstock=stock-int(i.qty)
                            mtdata.stock=newstock
                            mtdata.save()
                            if newstock == 0:
                                usr=tbl_user.objects.get(id=request.session['uid'])
                                data=tbl_mcart.objects.filter(mbooking__status=0,material=mtdata).exclude(mbooking__user=usr)
                                for i in data:
                                    tbl_mcart.objects.get(id=i.id).delete()
                                mdata.status=1
                                mdata.save()
                            else:
                                mdata.status=1
                                mdata.save() 
                        return redirect("User:processingpayment")
                
            elif 'bookings' in request.session:
                ids=tbl_wbooking.objects.get(id=request.session["bookings"])
                ids.status=1
                ids.save()
                return redirect("User:processingpayment")
            else:
                mdata=tbl_mbooking.objects.get(id=request.session["mbookings"])
                mcartdatacount=tbl_mcart.objects.filter(mbooking=mdata).count()
                if mcartdatacount>0:
                    mcartdata=tbl_mcart.objects.filter(mbooking=mdata)
                    for i in mcartdata:
                        mtdata=tbl_material.objects.get(id=i.material.id)
                        stock=int(mtdata.stock)
                        newstock=stock-int(i.qty)
                        mtdata.stock=newstock
                        mtdata.save()
                        if newstock == 0:
                            usr=tbl_user.objects.get(id=request.session['uid'])
                            data=tbl_mcart.objects.filter(mbooking__status=0,material=mtdata).exclude(mbooking__user=usr)
                            for i in data:
                                tbl_mcart.objects.get(id=i.id).delete()
                            mdata.status=1
                            mdata.save()
                        else:
                            mdata.status=1
                            mdata.save()
                    return redirect("User:processingpayment")
                else:
                    return render(request,"User/Payment.html")
            
        else:
                return render(request,"User/Payment.html")
    else:    
        return redirect("Guest:login")
            
        

def processingpayment(request):
    if 'uid' in request.session:
        return render(request,"User/runpayment.html")
    else:
        return redirect("Guest:login")
   
def paysucess(request):
   if 'uid' in request.session:
        return render(request,"User/paysucessful.html")
   else:
       return redirect("Guest:login")
    
#---------My bookings------------

def mybookings(request):

    if 'uid' in request.session:

        usr=tbl_user.objects.get(id=request.session["uid"])
        data=tbl_wcart.objects.filter(wbooking__user=usr)
       
        #material booking display
        mdata=tbl_mcart.objects.filter(mbooking__user=usr)
        return render(request,"User/MyBookings.html",{'data':data,'mdata':mdata})
    else:
        return redirect("Guest:login")

def removecart(request,did):
    tbl_wcart.objects.get(id=did).delete()
    return redirect('User:mycart')
def removecart1(request,did):
    tbl_mcart.objects.get(id=did).delete()
    return redirect('User:mycart')
def starrating(request,mid):
    parray=[1,2,3,4,5]
    mid=mid
    cdata=tbl_wcart.objects.get(id=mid)
    wid=cdata.works.id
    wdata=tbl_work.objects.get(id=wid)
    counts=0
    counts=tbl_star.objects.filter(work_id=wdata).count()
    if counts>0:
        res=0
        stardata=tbl_star.objects.filter(work_id=wdata).order_by('-datetime')
        for i in stardata:
            res=res+i.rating_data
        avg=res//counts
        return render(request,"User/WorkRating.html",{'mid':mid,'data':stardata,'ar':parray,'avg':avg,'count':counts})
    else:
         return render(request,"User/WorkRating.html",{'mid':mid})

def ajaxstar(request):
    parray=[1,2,3,4,5]
    rating_data=request.GET.get('rating_data')
    user_name=request.GET.get('user_name')
    user_review=request.GET.get('user_review')
    workid=request.GET.get('workid')
    cdata=tbl_wcart.objects.get(id=workid)
    wid=cdata.works.id
    wdata=tbl_work.objects.get(id=wid)
    tbl_star.objects.create(user_name=user_name,user_review=user_review,rating_data=rating_data,work_id=wdata)
    stardata=tbl_star.objects.filter(work_id=wdata).order_by('-datetime')
    return render(request,"User/AjaxRating.html",{'data':stardata,'ar':parray})
        

def deliver(request):
    message=request.session["mess"]
    return render(request,"User/DeliveryTravel.html",{'mess':message})


def bill(request):
    if 'uid' in request.session:
        usr=tbl_user.objects.get(id=request.session["uid"])
        total=0
        if 'bookings' in request.session and 'mbookings' in request.session:
            rand=random.randint(100000,999999)
            cdate=date.today()
            bookdata=tbl_wbooking.objects.get(id=request.session["bookings"])
            mbookdata=tbl_mbooking.objects.get(id=request.session["mbookings"])
            mcartdata=tbl_mcart.objects.filter(mbooking=mbookdata)
            wcartdata=tbl_wcart.objects.filter(wbooking=bookdata)
            for i in wcartdata:
                total=total+(int(i.qty)*int(i.works.rate))
            for j in mcartdata:
                total=total+(int(j.qty)*int(j.material.rate))
            
            return render(request,"User/bill.html",{'mdata':mcartdata,'wdata':wcartdata,'rand':rand,'cdate':cdate,'usr':usr,'total':total})
        elif 'bookings' in request.session:
            rand=random.randint(100000,999999)
            cdate=date.today()
            bookdata=tbl_wbooking.objects.get(id=request.session["bookings"])
            wcartdata=tbl_wcart.objects.filter(wbooking=bookdata)
            for i in wcartdata:
                total=total+(int(i.qty)*int(i.works.rate))
            
            return render(request,"User/bill.html",{'wdata':wcartdata,'rand':rand,'cdate':cdate,'usr':usr,'total':total})
        elif 'mbookings' in request.session:
            rand=random.randint(100000,999999)
            cdate=date.today()
            mbookdata=tbl_mbooking.objects.get(id=request.session["mbookings"])
            mcartdata=tbl_mcart.objects.filter(mbooking=mbookdata)
            for i in mcartdata:
                total=total+(int(i.qty)*int(i.material.rate))
            
            return render(request,"User/bill.html",{'mdata':mcartdata,'rand':rand,'cdate':cdate,'usr':usr,'total':total})
        else:
            return render(request,"User/bill.html")
    else:
        return redirect("Guest:login")

def chatuser(request, cid):
    chatobj = tbl_wcart.objects.get(id=cid)
    if request.method == "POST":
        cied = request.POST.get("cid")
        # print(cied)
        ciedobj = tbl_seller.objects.get(id=cied)
        sobj = tbl_user.objects.get(id=request.session["uid"])
        content = request.POST.get("msg")
        # print(cied)
        # print(content)
        Chat.objects.create(
            from_user=sobj, to_seller=ciedobj, content=content, from_seller=None, to_user=None)
        return render(request, 'User/Chat.html', {"chatobj": chatobj})
    else:
        return render(request, 'User/Chat.html', {"chatobj": chatobj})

def loadchatuser(request):
    cid = request.GET.get("cid")
    request.session["cid"] = cid

    cid1 = request.session["cid"]
    # print(cid1)

    # print(cid)
    shopobj = tbl_seller.objects.get(id=cid)
    # print(userobj)
    sid = request.session["uid"]
    # print(sid)
    suserobj = tbl_user.objects.get(id=request.session["uid"])
    # chatobj1 = Chat.objects.filter(Q(to_user=suserobj) | Q(
    #     from_user=suserobj), Q(to_shop=shopobj) | Q(from_shop=shopobj))
    # print(chatobj1)  # send message

    # print(chatobj2)  # recived msg
    chatobj = Chat.objects.raw(
        "select * from User_chat c inner join Guest_tbl_user u on (u.id=c.from_user_id) or (u.id=c.to_user_id) WHERE  c.from_seller_id=%s or c.to_seller_id=%s order by c.date", params=[(cid1), (cid1)])

    print(chatobj.query)

    return render(request, 'User/Load.html', {"obj": chatobj, "sid": sid, "shop": shopobj, "userobj": suserobj})

def videopay(request,id):
    userdata=tbl_user.objects.get(id=request.session['uid'])
    sellerdata=tbl_seller.objects.get(id=request.session['id'])
    vpaydata=tbl_videopay.objects.filter(seller=sellerdata,user=userdata).count()
    
    return render(request,'User/Videopay')

   





from django.urls import path
from User import views

app_name='User'

urlpatterns = [
    path('UserHome/',views.userhome,name="UserHome"),
    path('MyProfile/',views.myprofile,name="MyProfile"),
    path('EditProfile/',views.editprof,name="EditProfile"),
    path('ChangePassword/',views.changepass,name="ChangePassword"),
    path('ViewWorks/<int:sid>',views.viewwork,name="ViewWorks"),
    path('SearchSeller/',views.searchsell,name="SearchSeller"),
    path('addtocart/<int:wid>',views.addtocart,name="addtocart"),
    path('MyCart/',views.mycart,name="mycart"),
    path('AddtoCartMaterial/<int:mid>',views.addtocartmaterial,name="addtocartmaterial"),
    path('ViewMaterial/<int:sid>',views.viewworkmaterial,name="ViewWorkMaterial"),
    path("mycart/",views.mycart, name="mycart"),
    path('getqnty/',views.get_qnty,name="GetQty"),
    path('getqnty1/',views.get_qnty1,name="GetQty1"),
    path('removeqty/<int:did>',views.removecart,name="removeqty"),
    path('removeqty1/<int:did>',views.removecart1,name="removeqty1"),
    path('payment/',views.PAYMENT,name="payment"),
    path('processingpayment/',views.processingpayment,name="processingpayment"),
    path('patmentsucessful/',views.paysucess,name="patmentsucessful"),
    path('Mybookings/',views.mybookings,name="my_bookings"),
    path('deliver/',views.deliver,name="deliver"),
    path('bill/',views.bill,name="bill"),
        path('AjaxWork/', views.AjaxWork,name="AjaxWork"),
    path('Chat/<int:cid>/', views.chatuser, name="Chat-user"),
    path('loadchat/', views.loadchatuser, name="load-chat"),
    path('star/<int:mid>',views.starrating,name="starrating"),
    path('ajaxstar/',views.ajaxstar,name="ajaxstar"),
    path('videopay/<int:id>',views.videopay,name="videopay"),
    path('complaint/',views.complaint,name="complaint"),
    path('delcomplaint/<int:did>',views.DeleteComplaint,name="delcomplaint"),
 
    
]
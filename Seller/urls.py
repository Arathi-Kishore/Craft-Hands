from django.urls import path
from Seller import views

app_name='Seller'

urlpatterns = [
    path('SellerHome/',views.sellerhome,name="SellerHome"),
    path('MyProfile/',views.myprofile,name="MyProfile"),
    path('EditProfile/',views.editprof,name="EditProfile"),
    path('ChangePassword/',views.changepass,name="ChangePassword"),
    path('AddWork/',views.addwork,name="AddWork"),
    path('AddMaterial/<int:wid>',views.addmat,name="AddMaterial"),
    path('del_materialdata/<int:did>',views.DeleteMaterial,name="deletematerial"),
    path('WorkGallery/<int:wid>',views.wgall,name="WorkGallery"),
    path('del_workdata/<int:did>',views.DeleteWork,name="deletework"),
    path('userbooking/',views.userbooking,name="Userbooking"),
    path('materialbooking/',views.materialbooking,name="materialbooking"),
  path('acceptorder/<int:aid>', views.acceptorder,name="acceptorder"),
    path('rejectorder/<int:rid>', views.rejectorder,name="rejectorder"),
    path('acceptwork/<int:aaid>', views.acceptwork,name="acceptwork"),
    path('rejectwork/<int:rrid>', views.rejectwork,name="rejectwork"),
    path('Chat/<int:cid>/', views.chatuser, name="Chat-user"),
    path('loadchat/', views.loadchatuser, name="load-chat"),
    path('complaint/',views.complaint,name="complaint"),
    path('delcomplaint/<int:did>',views.DeleteComplaint,name="delcomplaint"),



path('itempacked/<int:pid>',views.itempacked,name="itempacked"),
    path('itemshipped/<int:shid>',views.itemshipped,name="itemshipped"),
    path('itemdispatched/<int:did>',views.itemdispatched,name="itemdispatched"),
    path('delivered/<int:ddid>',views.delivered,name="delivered"),
    #material
    path('mitempacked/<int:pid>',views.mitempacked,name="mitempacked"),
    path('mitemshipped/<int:shid>',views.mitemshipped,name="mitemshipped"),
    path('mitemdispatched/<int:did>',views.mitemdispatched,name="mitemdispatched"),
    path('mdelivered/<int:ddid>',views.mdelivered,name="mdelivered"),
# report
    path('workreport/',views.workreport,name="workreport"),
    path('videopay/',views.videoreport,name="videopay"),
    path('materialreport/',views.materialreport,name="materialreport"),
    path('viewreason/<int:mid>',views.viewreason,name="viewreason"),
    path('verifyreason/<int:rid>',views.verifyreason,name="verifyreason"),
    path('wviewreason/<int:wid>',views.wviewreason,name="wviewreason"),
    path('wverifyreason/<int:pid>',views.wverifyreason,name="wverifyreason"),
    path('logout/',views.logout,name="logout"),

     path('weeklyreport/',views.weekly_booking_report,name="weekly"),
    path('monthlyreport/',views.monthly_booking_report,name="monthly"),
    path('yearlyreport/',views.yearly_booking_report,name="yearly"),
]   
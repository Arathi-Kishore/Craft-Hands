from django.urls import path
from Admin import views
from Guest import *

app_name='Admin'
urlpatterns=[
    path('district/',views.dis,name="District"),
    path('del_district/<int:did>',views.DeleteDistrict,name="del_district"),
    path('edit_district/<int:eid>',views.EditDistrict,name="edit_district"),
    path('place/',views.pla,name="Place"),
    path('del_place/<int:did>',views.DeletePlace,name="del_place"),
    path('ajaxplace/',views.ajaxplace,name="ajaxplace"),
    path('location/',views.loc,name="Location"),
    path('del_loc/<int:did>',views.Deletelocation,name="del_location"),
    path('work/',views.WorkType,name="WorkType"),
    path('del_work/<int:did>',views.DeleteWork,name="del_work"),
    path('edit_work/<int:eid>',views.EditWork,name="edit_work"),
    path('viewsellerlist/',views.sellerlist,name="ViewSellerList"),
    path('acceptedlist/',views.acceptlist,name="AcceptedList"),
    path('rejectedlist/',views.rejectlist,name="RejectedList"),
    path('acceptlist/<int:aid>',views.accept,name="acceptlist"),
    path('rejectlist/<int:rid>',views.reject,name="rejectlist"),
    path('adminhome/',views.adminhome,name="AdminHome"),

]
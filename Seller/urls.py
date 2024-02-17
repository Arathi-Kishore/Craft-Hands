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
    
]   
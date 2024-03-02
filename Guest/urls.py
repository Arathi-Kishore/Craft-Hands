from django.urls import path
from Guest import views
app_name='Guest'
urlpatterns=[
    path('UserRegistration/',views.user,name="UserRegistration"),
    path('Login/',views.login,name="login"),
    path('ajaxloc/',views.ajaxlocation,name="ajaxloc"),
    path('SellerRegistration/',views.seller,name="SellerRegistration"),
    path('',views.index,name="index"),
    
    
]
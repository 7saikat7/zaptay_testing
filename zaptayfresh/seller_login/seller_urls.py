from django.urls import path, include

from seller_login import views

app_name = "seller_login"

urlpatterns = [
    path('', views.ShowsellerLogin.as_view() ,name="seller_loginpage"),  #login/
    path('seller_dashboard/', views.SellerDashBoard.as_view(), name="sellerdashboard"),  #dashboard/
    path('logout/', views.Logout, name="logout"),  # logout/
    path('AddProd/', views.Aprod.as_view(), name="addProduct"),  # Add Product/
    path('SellerDash/', views.SellerDash.as_view(), name="SellerDash"),  # SellerDash/
    path('orderListWaiting/', views.orderListWaiting.as_view(), name="orderListWaiting"),  # orderList/
    path('orderListSold/', views.orderListSold.as_view(), name="orderListSold"),  # orderList/
    path('SellerReturn/', views.SellerReturn.as_view(), name="SellerReturn"),  # SellerReturn/

    path('ResetPwd/', views.ResetPwd.as_view(), name="ResetPwd"),
    path('Return/', include('Return.urls'))

 


    
    
]
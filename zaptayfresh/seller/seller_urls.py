from django.urls import path, include, re_path
from seller import views

app_name = "seller"

urlpatterns = [
    path('all-seller/', views.ViewSellerList.as_view(), name="all_seller"),
    path('seller-view/<str:seller_id>', views.ViewSeller.as_view(), name="seller_view"),
    path('add-seller/', views.AddSellerForm.as_view(), name="add_seller"),
    path('edit-seller/<str:seller_id>', views.EditSeller.as_view(), name="edit_seller"),
    path('SellerDashBoard/<str:seller_id>', views.SellerDashBoard.as_view(), name="SellerDashBoard"),
    path('SellerDatabase/<str:seller_id>', views.SellerDatabase.as_view(), name="SellerDatabase"),



    # Ajax
    path('SellerDel/' ,views.SellerDel , name="SellerDel"),
    path('activatesel/' ,views.SellerActivate , name="SellerActivate"),
    path('Deactivatesel/', views.SellerDeactivate, name="SellerDeactivate"),
    
    path('ProductActivate/' ,views.ProductActivate , name="ProductActivate"),
    path('ProductDeactivate/' ,views.ProductDeactivate , name="ProductDeactivate"),



   
]
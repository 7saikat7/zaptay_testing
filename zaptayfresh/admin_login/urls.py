from django.urls import path, include

from admin_login import views

app_name = "admin_login"

urlpatterns = [
    path('', views.ShowadminLogin.as_view() ,name="admin_loginpage"),  #login/
    path('dashboard/', views.DashBoard.as_view(), name="dashboard"),  #dashboard/
    path('logout', views.Logout, name="logout"),  # logout/
    path('ResetPwd/', views.ResetPwd.as_view(), name="ResetPwd"),

    # other apps
    path('seller/', include('seller.seller_urls'), name="seller"),
    path('attribute/', include('attribute.admin_urls'), name="attribute"),
    path('product/', include('zap_product.admin_urls'), name="product"),
    path('banner/', include('banner.admin_urls'),name="banner"),
    path('offer/', include('offer.admin_urls')),
    path('Policy/', include('zap_policy.urls'))


    
    
]

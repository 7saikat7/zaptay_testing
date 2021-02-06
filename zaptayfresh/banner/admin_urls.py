from django.urls import path, include
from banner import views

app_name = "banner"

urlpatterns = [
    path('', views.ViewBanner.as_view(), name="banner_list"),
    path('website-logo/', views.WebSiteLogo.as_view(), name="website_logo"),

    # Ajax URLField
    path('banner-delete/', views.DeleteBannerImage, name="delete_banner_image"),
    path('banner-ad-delete/', views.DeleteadBannerImage, name="delete_banner_ad_image"),
]

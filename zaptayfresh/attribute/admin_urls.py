from django.urls import path, include, re_path
from attribute import views

app_name = "attribute"

urlpatterns = [
    path('', views.AttributeList.as_view(), name="attribute"),
    path('colimg/', views.setcolImage, name="colimg"),
    path('brandimg/', views.setbrandImage, name="brandimg"),



    # Ajax url
    path('add-main-category/', views.AddMainCategory.as_view(), name="admin_add_category"),
    path('show-all/', views.ShowAllMainCategory.as_view(), name="admin_show_main_categorypage"),
    path('add-sub-category/', views.AddSubCategory.as_view(), name="admin_add_sub_category"),
    path('get-cateory', views.SendCategoryData, name="ajax_category"),
    path('get-sub-cateory', views.SendSubCategoryData, name="ajax_sub-category"),
    path('get-tert-cateory', views.SendTertiaryCategoryData, name="ajax_tert-category"),
    path('delete-attributes/', views.DeleteAttrinutsData, name="ajax_attribute_del"),

    path('get-sorted-sub-category/', views.SendSortSubCategory, name='sort_sub_category'),
    path('get-sorted-terti-category/', views.TertiarySubCategory, name='sort_terti_category'),
    path('get-sorted-under-terti-category/', views.SendUnderTertiaryCategory, name='sort_under_terti_category'),
    path('get-all-brand/', views.GetAllBrands, name='get_all_brand'),
    path('get-all-color/', views.GetAllColors, name='get_all_colors'),
    path('get-all-size/', views.GetAllSize, name='get_all_size'),
    path('get-all-made-in/', views.GetAllMadeIn, name='get_all_made_in'),
    # re_path(r'^get-sorted-sub-category/(?P<category_id>[0-9])/$', views.SendSortSubCategory, name='sort_sub_category'),

    path('get-subcategory-details', views.GetSubCategoryDetails, name="get_subcategory_details"),
    path('subcategory-image/', views.AjaxImageUpload, name="subcategory_image"),
]

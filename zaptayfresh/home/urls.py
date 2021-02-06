from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from home import views

app_name = 'home'

urlpatterns = [

    
    path('', views.MainHome.as_view(), name="homepage"),
    path('singleproduct/<slug:Product_iD>',views.singleProduct.as_view(),name="singleproduct"),
    path('subcategory/<uuid:sucat_id>',views.SubCategoryProductView.as_view(),name="subcategory"),
    path('Indianhatt/',views.IndianHatt.as_view(),name="indianHatt"),
    path('b2b/', views.b2b.as_view(), name="b2b"),
    path('update_item/',views.updateItem,name='update_item'),


    #LOGIN
    path('ShowuserLogin/', views.ShowuserLogin,name="user_loginpage"),
    # path('ShowuserSignup/', views.ShowuserSignup.as_view() ,name="user_signuppage"),  #login/
    path('ShowuserSignup/', views.ShowuserSignup,name="user_signuppage"),
    path('user_logout/', views.user_Logout, name="user_logout"),  # logout/
    path('ResetPwd/', views.ResetPwd.as_view(), name="ResetPwd"),
    path('activate/<uidb64>/<token>/',views.Verificationview.as_view(),name="activate"),
    

    path('vieall/<slug:name>',views.viewall.as_view(),name="viewall"),
    path('vieallSubCat/<slug:name>',views.viewallSubCategory.as_view(),name="viewallSuCat"),
    # path('wish-list/', include('wishlist.urls')),
    # path('cart-list/', include('cart.urls')),

   ########  for  shopping cart ########
  

    # Ajax
    # Views Counter
    path('customerView/', views.CustomerView, name="CustomerView"),

    # home page
    path('bannerjson/', views.bannerJasonList.as_view(), name="bannrjson"),
    path('bannerjsonspecific/',views.bannerJasonListspecific,name="bannerjsonspecific"),


    #single prod page
    path('relatedProdSingleProdpage/',views.relatedProdSingleProdpage,name="relatedProdSingleProdpage"),
    path('PODSingleProdpage/',views.PODSingleProdpage,name="PODSingleProdpage"),

    


    #sub category page
    path('underTer/',views.underTerAll.as_view(),name="underTer"),
    path('underTerspecific/',views.underTerspecific,name="underTerspecific"),
    path('allprod/',views.allproduct,name="allprod"),
    path('getprodbyBrand/',views.getprodbyBrand,name="getprodbyBrand"),
    path('getprodbySize/',views.getprodbySize,name="getprodbySize"),
    path('getprodbycolor/',views.getprodbycolor,name="getprodbycolor"),
    path('underTerprod/', views.underTerprod, name="underTerprod"),

    path('underTerprod/', views.underTerprod, name="underTerprod"),
    path('underTerprod/', views.underTerprod, name="underTerprod"),

    path('relatedProdSubCatpage/',views.relatedProdSubCatpage,name="relatedProdSubCatpage"),
    path('PODSubCatpage/',views.PODSubCatpage,name="PODSubCatpage"),


    #indian hatt
    path('Ihatttwntyprsnt/', views.Ihatttwntyprsnt, name="Ihatttwntyprsnt"),
    path('b2b/', views.b2b, name="b2b"),

    # view all offer
    path('viewall_offer/', views.viewalloffersMore, name="viewall_offer"),
    path('viewallofferscolFilter/', views.viewallofferscolFilter, name="viewallofferscolFilter"),
    # view all Subcat
    path('viewall_Subcat/', views.viewallSubcatMore, name="viewall_Subcat"),
    path('viewallSubcatcolrFilter/', views.viewallSubcatcolrFilter, name="viewallSubcatcolrFilter"),
    
    


]

 
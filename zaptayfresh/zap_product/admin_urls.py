from django.contrib import admin
from django.urls import path

from zap_product import views

app_name = 'product'

urlpatterns = [
    path('product-form/', views.ShowProductForm.as_view(), name="product_form"),
    path('product-edit-form/<str:Product_id>', views.EditProduct.as_view(), name="edit_product"),
    path('product-all/', views.ShowProductList.as_view(), name="product_all"),
    path('B2B/', views.B2Bview.as_view(), name="B2b"),



    # path('men/<slug:product_slug>/', views.ProductViews.as_view(), name="category-men"),
    # path('add-wish-list/', views.AddWishlist, name="add_wish_list"),
    # path('add-to-cart/', views.AddCart, name="add_to_cart"),
    path('<slug:product_slug>/', views.ProductViewsDetails.as_view(), name="show_product"),
    
]
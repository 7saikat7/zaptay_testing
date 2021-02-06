from django.urls import path, include
from offer import views

app_name = 'offer'

urlpatterns = [
     
    path('OfferView/<str:offer_id>', views.OfferView.as_view(), name='OfferViewid'),
    path('OfferView/', views.OfferView.as_view(), name='OfferView'),
    


    # Ajax
    path('OfferDel/',views.OfferDel,name='OfferDel'),



    
]
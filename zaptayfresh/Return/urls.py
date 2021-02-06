from django.urls import path, include
from Return import views

app_name = 'Return'

urlpatterns = [
    path('', views.retun.as_view(), name="Return"),
]
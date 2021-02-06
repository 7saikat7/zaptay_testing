from django.urls import path, include
from zap_policy import views

app_name = 'Policy'

urlpatterns = [
    path('', views.Policy.as_view(), name="Policy"),
    
]
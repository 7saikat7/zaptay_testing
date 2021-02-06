from django.contrib import admin
from seller.models import Seller

# Register your models here.
admin.site.register(Seller)

class SellerAdmin(admin.ModelAdmin):
    readonly_fields=['seller_id',]
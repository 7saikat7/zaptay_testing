from django.contrib import admin
from . models import Offer, OfferProduct

# Register your models here.
admin.site.register(Offer)
admin.site.register(OfferProduct)
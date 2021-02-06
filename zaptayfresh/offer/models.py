from django.db import models
from django.db.models.signals import pre_save
from admin_login.models import zaptayadmin
from zap_product.models import *
# from stock.models import Bach

from django.utils import timezone
from django.utils.timezone import now
from datetime import datetime
import time
from offer.utils import unique_Offer_ID ,unique_Offer_Prod_ID
# Create your models here.

class Offer(models.Model):
    offer_custom_id         = models.CharField(primary_key=True,max_length=150, unique=True , editable= False)
    offer_title             = models.CharField(max_length=250)
    offer_status            = models.CharField(max_length=100)
    is_active               = models.BooleanField(default=True)
    added_by                = models.ForeignKey(zaptayadmin, on_delete=models.CASCADE)
    modify_date             = models.DateTimeField(auto_now=True)
    create_date             = models.DateTimeField(auto_now_add=True)

    '''
    modify_date.editable=True
    create_date.editable=True
    '''

    class Meta:
        db_table = "offers"


    def __str__(self):
        return self.offer_title


def pre_save_offer_id(sender, instance, *args, **kwargs):
    if not instance.offer_custom_id:
        today =  datetime.today()
        instance.offer_custom_id = 'OFFER-'+str(today.year)+'-'+str(int(time.time()))+'-'+unique_Offer_ID(instance)

pre_save.connect(pre_save_offer_id, sender=Offer )





############################################ Offer Product Model ###########################################################
class OfferProduct(models.Model):
    offer_product_id        = models.CharField(primary_key=True,max_length=150, unique=True , editable= False)
    offer_id                = models.ForeignKey(Offer, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Productmod, on_delete=models.CASCADE)
    # bach_id               = models.ForeignKey(Bach, on_delete=models.CASCADE, blank=True, null=True)
    Product_offer_start     = models.DateTimeField(default=now)
    Product_offer_end       = models.DateTimeField(default=now)
    extra_offer_price       = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    added_by                = models.ForeignKey(zaptayadmin, on_delete=models.CASCADE)
    is_active               = models.BooleanField(default=True)
    modify_date             = models.DateTimeField(auto_now=True)
    create_date             = models.DateTimeField(auto_now_add=True)
    '''
    modify_date.editable=True
    create_date.editable=True
    '''

    class Meta:
        db_table = "offer_products"



    def __str__(self):
        return self.offer_product_id




def pre_save_offer_Prod_id(sender, instance, *args, **kwargs):
    if not instance.offer_product_id:
        today =  datetime.today()
        instance.offer_product_id = 'OFFER-PRO-'+str(today.year)+'-'+str(int(time.time()))+'-'+unique_Offer_Prod_ID(instance)

pre_save.connect(pre_save_offer_Prod_id, sender=OfferProduct )
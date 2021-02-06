from django.db import models
from django.db.models.signals import pre_save
from admin_login.models import zaptayadmin
from django.utils import timezone
from django.utils.timezone import now
from datetime import datetime
import time
from seller.utils import unique_sellerId_generator
import uuid
# Create your models here.

class Seller(models.Model):

    id                      = models.CharField(max_length=200,  blank=True,default=uuid.uuid4,  editable=False)
    seller_id               = models.CharField(primary_key=True,max_length=100,  editable=False)
    seller_CompanyName            = models.CharField(max_length=100)
    seller_name             = models.CharField(max_length=100)
    seller_email_id         = models.CharField(max_length=200)
    seller_phone_no         = models.CharField(max_length=200)
    seller_address          = models.TextField(default="")
    Seller_BankDetails      = models.TextField(default="")
    seller_specification    = models.CharField(max_length=100, default="")
    seller_gst_no           = models.CharField(max_length=200, blank=True, null=True)
    seller_PWD              = models.CharField(max_length=200, blank=True, null=True)
    seller_aadhaar_no       = models.CharField(max_length=200, blank=True, null=True)
    seller_voter_no         = models.CharField(max_length=100, blank=True, null=True)

    SellerImage             = models.FileField(upload_to="Seller/SellerImage")
    SellerAdhaarImage       = models.FileField(upload_to="Seller/SellerAdhaarImage" )
    SellerVoterImage        = models.FileField(upload_to="Seller/SellerVoterImage" )
    SellerGstImage          = models.FileField(upload_to="Seller/SellerGstImage")

 

    is_active               = models.BooleanField(default=1)
    added_by                = models.ForeignKey(zaptayadmin, on_delete=models.CASCADE)
    modify_date             = models.DateTimeField(default=now)
    create_date             = models.DateTimeField(default=now)

    class Meta:
        db_table = 'sellers'



    def __str__(self):
        return self.seller_id


def remove(string):
    return string.replace(" ", "")


def pre_save_create_seller_id(sender, instance, *args, **kwargs):
    if not instance.seller_id:
        today =  datetime.today()
        instance.seller_id = 'SELLER-'+str(today.year)+'-'+str(remove(instance.seller_name.upper()))+'-'+unique_sellerId_generator(instance)

pre_save.connect(pre_save_create_seller_id, sender=Seller )
from django.db import models
from django.db.models.signals import pre_save
from attribute.models import *
from seller.models import Seller
from admin_login.models import zaptayadmin

from django.utils import timezone
from django.utils.timezone import now
from datetime import datetime
import time

from zap_product.utils import *

# Create your models here.

class Productmod(models.Model):
    prod_custom_id                  = models.CharField(primary_key=True,max_length=200, unique=True , editable= False)
    prod_title                      = models.CharField(max_length=250)

    prod_category                   = models.ForeignKey(MainCategory, on_delete=models.CASCADE, blank=False, null=False)
    prod_sub_category               = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=False)
    prod_tertiary_category          = models.ForeignKey(TertiaryCategory, on_delete=models.CASCADE, blank=True, null=True)
    prod_under_tertiary_category    = models.ForeignKey(UnderTertiaryCategory, on_delete=models.CASCADE, blank=True, null=True)
    prod_brand                      = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=False, null=False)

    prod_made_in                    = models.ForeignKey(MadeIn, on_delete=models.CASCADE, blank=False)
    prod_desc                       = models.TextField(blank=False)
    seller                          = models.ForeignKey(Seller, on_delete=models.CASCADE)

    same_day_delivery               = models.BooleanField(default=False)
    same_day_delivery_price         = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    next_day_delivery               = models.BooleanField(default=False)
    next_day_delivery_price         = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    customize_day_delivery          = models.BooleanField(default=False)
    customize_day_delivery_day      = models.IntegerField(blank = True)
    customize_day_delivery_price    = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    product_return                  = models.BooleanField(default=False)
    cash_on_delivery                = models.BooleanField(default=False)
    is_active                       = models.BooleanField(default=1)
    added_by                        = models.ForeignKey(zaptayadmin, on_delete=models.CASCADE)
    modify_date                     = models.DateTimeField(default=now)
    create_date                     = models.DateTimeField(default=now)

    m_price                         = models.DecimalField(max_digits=10, decimal_places=2,default=0.00, blank=False)
    is_add2offer                    = models.BooleanField(default=1)
    off_price                       = models.DecimalField(max_digits=10, decimal_places=2,default=0.00, blank=False)

    is_b2b                          = models.BooleanField(default=1)


    stock                           = models.IntegerField(default=0)


    prod_image_id                   = models.CharField(max_length=200, unique=False)  #for tracking its own main form images
    prod_track_id                   = models.CharField(max_length=200, unique=False)  #for tracking its own other products
    MCproduct                       = models.CharField(max_length=200, unique=False)  #for tracking its mother(main) or child(sub)
    sizetrack                       = models.CharField(max_length=200, unique=False)  #for tracking its size



    product_image                   = models.ImageField(upload_to="products/images", )
    product_image1                   = models.ImageField(upload_to="products/images", )
    product_image2                   = models.ImageField(upload_to="products/images", )
    product_image3                   = models.ImageField(upload_to="products/images", )
    product_image4                   = models.ImageField(upload_to="products/images", )
    product_image5                   = models.ImageField(upload_to="products/images", )
    product_image6                   = models.ImageField(upload_to="products/images", )



    youtube_link                    = models.URLField(max_length=300, blank=True)
    prod_color                      = models.ForeignKey(Colour, on_delete=models.CASCADE,  blank=False)
    prod_size                       = models.ForeignKey(Size, on_delete=models.CASCADE,   blank=True)

    Cutomer_Views = models.BigIntegerField(default=512)
    is_approved                          = models.BooleanField(default=0)







    #Fields added for offer app showing
    Product_offer_start     = models.DateTimeField(default=now)
    Product_offer_end       = models.DateTimeField(default=now)
    extra_offer_price       = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Offer_Name              = models.CharField(max_length=200, null=True, blank=True)





    class Meta:
        db_table = 'zap_productss'



    def __str__(self):
        return self.prod_custom_id




def remove(string):
    return string.replace(" ", "")


def pre_save_Prod_id(sender, instance, *args, **kwargs):

    if not instance.prod_custom_id:
        today =  datetime.today()
        instance.prod_custom_id = 'PROD-'+str(today.year)+'-'+str(remove(instance.prod_title.upper()))+'-'+unique_Product_ID(instance)


pre_save.connect(pre_save_Prod_id, sender=Productmod)





class prodSize(models.Model):
    prodsize_id = models.UUIDField(primary_key=True,max_length=100,)
    size_name = models.CharField(max_length=50, blank=True, null=True)
    trackidSize = models.CharField(max_length=500, blank=True, null=True) #stores prod size track id

    product = models.ForeignKey(Productmod, on_delete=models.CASCADE)



    class Meta:
        db_table = "productsizes"


    def __str__(self):
        return self.size_name

from django.db import models
from django.utils import timezone
from django.utils.timezone import now
from datetime import datetime

from zap_product.models import *

import uuid
# Create your models here.
 

class zaptayuser(models.Model):
    id = models.UUIDField(primary_key = True,  default=uuid.uuid4, editable=False)
    user_name = models.CharField(max_length=50)
    email_id = models.CharField(max_length=100)
    password = models.CharField(max_length=254)
    phone_no = models.BigIntegerField( )
    modify_date = models.DateTimeField(default=now)
    create_date = models.DateTimeField(default=now)

    class Meta:
        db_table = 'zaptay_user'
    
    

    def __str__(self):
        return self.email_id

class wishlist(models.Model):
    user = models.ForeignKey(zaptayuser,on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Productmod, on_delete=models.SET_NULL, null=True)

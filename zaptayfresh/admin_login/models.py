from django.db import models
from django.utils import timezone
from django.utils.timezone import now
from datetime import datetime

import uuid
# Create your models here.
 


class zaptayadmin(models.Model):
    id = models.UUIDField(primary_key = True,  default=uuid.uuid4, editable=False)
    admin_f_name = models.CharField(max_length=50)
    admin_l_name = models.CharField(max_length=50)
    admin_type = models.CharField(max_length=20)
    is_active = models.BooleanField(default=1)
    email_id = models.CharField(max_length=100)
    password = models.CharField(max_length=254)
    phone_no = models.BigIntegerField( )
    modify_date = models.DateTimeField(default=now)
    create_date = models.DateTimeField(default=now)

    class Meta:
        db_table = 'zaptay_admin'
    
    

    def __str__(self):
        return self.email_id

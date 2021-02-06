from django.db import models
from admin_login.models import zaptayadmin

from datetime import datetime
import time
import uuid

# Create your models here.

class Banner(models.Model):
    banner_id = models.CharField(max_length=100, blank=True, null=True)
    banner_image = models.ImageField(upload_to="banner/images", default="", blank=True, null=True)
    banner_name = models.CharField(max_length=50, blank=True, null=True)
    banner_name_custom = models.CharField(max_length=50, blank=True, null=True)
    banner_link = models.URLField(max_length = 200, blank=True, null=True)
    added_by = models.ForeignKey(zaptayadmin, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(auto_now=True)
    added_date = models.DateTimeField(auto_now_add=True)
    # added_date.editable=True

    class Meta:
        db_table = "banners"

    def save(self, *args, **kwargs):
        if self.banner_id == None:
            if len(Banner.objects.all().order_by('-id')) == 0:
                get_max_id = 0
                mod_id = get_max_id+1
            else:
                get_max_id = Banner.objects.all().order_by('-id')[0]
                mod_id = get_max_id.id+1
            mod_id = str(mod_id).zfill(6)
            today = datetime.today()
            self.banner_id = 'BAN-'+str(today.year)+'-'+str(int(time.time()))+'-'+str(mod_id)
        super(Banner, self).save(*args, **kwargs)

    def __str__(self):
        return self.banner_name




class webLogo(models.Model):
    webid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    banner_image = models.ImageField(upload_to="banner/websiteHeadLogo", default="", blank=True, null=True)
    banner_name = models.CharField(max_length=50, blank=True, null=True)
   
    
    class Meta:
        db_table = "weblogo"

    def __str__(self):
        return self.banner_name


class adactive(models.Model):
    banner_id = models.CharField(max_length=100, blank=True, null=True)
    banner_image = models.ImageField(upload_to="banner/images/adactive", default="", blank=True, null=True)
    banner_name = models.CharField(max_length=50, blank=True, null=True)
    banner_name_custom = models.CharField(max_length=50, blank=True, null=True)
    banner_link = models.URLField(max_length = 200, blank=True, null=True)
    added_by = models.ForeignKey(zaptayadmin, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(auto_now=True)
    added_date = models.DateTimeField(auto_now_add=True)
    # added_date.editable=True
    
    
    class Meta:
        db_table = "adactive"



    def save(self, *args, **kwargs):
        if self.banner_id == None:
            if len(adactive.objects.all().order_by('-id')) == 0:
                get_max_id = 0
                mod_id = get_max_id+1
            else:
                get_max_id = adactive.objects.all().order_by('-id')[0]
                mod_id = get_max_id.id+1
            mod_id = str(mod_id).zfill(6)
            today = datetime.today()
            self.banner_id = 'BAN-ADACTIVE-'+str(today.year)+'-'+str(int(time.time()))+'-'+str(mod_id)
        super(adactive, self).save(*args, **kwargs)

    def __str__(self):
        return self.banner_name

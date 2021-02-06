from django.apps import AppConfig
from django.contrib import admin

from admin_login.models import zaptayuser

class HomeConfig(AppConfig):
    name = 'home'



# Register your models here.


class zaptay_user(admin.ModelAdmin):
    list_display = ('admin_f_name','admin_l_name','id','email_id','password',  'phone_no', 'modify_date', 'create_date')





admin.site.register(zaptayuser  , zaptay_user)
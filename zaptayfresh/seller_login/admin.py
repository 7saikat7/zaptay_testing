from django.contrib import admin

from seller_login.models import seller_login
# Register your models here.


class seller_log(admin.ModelAdmin):
    list_display = ('seller_f_name','seller_l_name','id',  'is_active', 'email_id','password',  'phone_no', 'modify_date', 'create_date')





admin.site.register(seller_login  , seller_log)
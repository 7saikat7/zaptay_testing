from django.contrib import admin

from admin_login.models import zaptayadmin
# Register your models here.


class zaptay(admin.ModelAdmin):
    list_display = ('admin_f_name','admin_l_name','id',   'admin_type','is_active', 'email_id','password',  'phone_no', 'modify_date', 'create_date')





admin.site.register(zaptayadmin  , zaptay)
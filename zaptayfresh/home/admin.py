from django.contrib import admin


from home.models import zaptayuser
# Register your models here.
# Register your models here.


class zaptay_user(admin.ModelAdmin):
    list_display = ('user_name','id','email_id','password',  'phone_no', 'modify_date', 'create_date')


admin.site.register(zaptayuser  , zaptay_user)
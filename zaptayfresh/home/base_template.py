#from banner.models import Banner
#from category.models import MainCategory
from attribute.models import *
#from user_login.models import UserAccount

from django.views.generic import *

class BaseTemplateHeader:
    def __init__(self, data):
        self.request = data

    def GetHeaderContent(self):
        #header_logo = get_header_logo = Banner.objects.filter(banner_name='header_logo').order_by('-id').first()

        megamenu = list()
        featured_category = MainCategory.objects.filter(main_category_name='featured').first()
        get_sub_category = SubCategory.objects.filter(category_id=featured_category)
        for i in get_sub_category:
            sub_category = list()
            sub_category.append({'name': i.sub_category_name, 'seo_url': i.sub_category_seo_url})
            get_tertiary_category = TertiaryCategory.objects.filter(sub_category_id=i)
            tertiary_cate_ar = list()
            for j in get_tertiary_category:
                tertiary_cate = dict()
                tertiary_cate['id'] = j.ter_category_id
                tertiary_cate['name'] = j.ter_category_name
                tertiary_cate_ar.append(tertiary_cate)
            sub_category.append(tertiary_cate_ar)
            megamenu.append(sub_category)
        # print (megamenu)

        #featured_category = MainCategory.objects.filter(main_category_name='exclusive').first()
        get_more_sub_category = SubCategory.objects.filter(category_id=featured_category)
        # print (featured_category)

        # Login User
        login_user_details = dict()
        login_user_details['status'] = 0
        if self.request.COOKIES.get('login_user_id'):
            get_user_id = self.request.COOKIES['login_user_id']
            login_user_details['user_id'] = get_user_id
            get_login_user_details = UserAccount.objects.filter(user_custom_id=get_user_id).first()
            login_user_details['user_name'] = get_login_user_details.user_f_name
            login_user_details['user_email'] = get_login_user_details.email_id
            login_user_details['status'] = 1

        response_data = dict()
        #response_data['header_logo'] = header_logo
        response_data['mega_menu_sub_category'] = megamenu
        response_data['mega_menu_more_category'] = get_more_sub_category
        response_data['login_user'] = login_user_details

        return response_data
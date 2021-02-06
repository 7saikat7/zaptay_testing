from django.shortcuts import render
from django.views.generic import *


# Models Import
from banner.models import *
from offer.models import *
from attribute.models import *
from zap_product.models import *
# Models Import End




# Create your views here.



class LoginView(TemplateView):
    template_name = "user_templates/user_login/user_login.html"


    def get_context_data(self, **kwargs):
        Offers_all = Offer.objects.all()
        produ = Productmod.objects.all()

        subCat = SubCategory.objects.all()
        terCat = TertiaryCategory.objects.all()
        # print(Offers_all)
        # print(subCat)
        # print(terCat)
        # for i in terCat:
        #     print(i.sub_category_id.sub_category_name)
        banners_head = webLogo.objects.filter(banner_name='header_logo').first()



        context = {
            'offers': Offers_all,
            'product': produ,
            'Subcat': subCat,
            'Tercat': terCat,
            'baner_head': banners_head,

        }
        return context





class SignupView(TemplateView):
    template_name = "user_templates/user_login/user_signup.html"

    def get_context_data(self, **kwargs):
        Offers_all = Offer.objects.all()
        produ = Productmod.objects.all()

        subCat = SubCategory.objects.all()
        terCat = TertiaryCategory.objects.all()
        # print(Offers_all)
        # print(subCat)
        # print(terCat)
        # for i in terCat:
        #     print(i.sub_category_id.sub_category_name)
        banners_head = webLogo.objects.filter(
            banner_name='header_logo').first()

        context = {
            'offers': Offers_all,
            'product': produ,
            'Subcat': subCat,
            'Tercat': terCat,
            'baner_head': banners_head,
        }
        return context
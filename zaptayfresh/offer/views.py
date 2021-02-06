from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import *
from django.contrib import messages

from django.db.models import Q, Subquery
from .models import *
from zap_product.models import *
from offer.forms import *
# from stock.models import Bach

from admin_login.models import *

# Create your views here.
# Admin views =============================================================================


class OfferView(TemplateView):
    template_name = 'admin_templates/admin_offer_templates/offer_Seller.html'

    def dispatch(self, request, *args, **kwargs):
        try:
            resp = request.session['admin_email_id']
            return super(OfferView, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)
            # return redirect('/site-admin/stock/')
            return redirect('admin_login:admin_loginpage')

    def get_context_data(self, **kwargs):
        frm = OfferSelect()
        context = dict()
        get_name = zaptayadmin.objects.all().get(email_id=self.request.session['admin_email_id'])
        get_offer_list = Offer.objects.all()
        get_ProductList = Productmod.objects.all().filter(is_add2offer=True)
        context = {
            "page_name": "offer",
            "admin_name": get_name.admin_f_name + " " + get_name.admin_f_name,
            'offers': get_offer_list,
            'frm': frm,
            'prod': get_ProductList,
        }
        return context

    def post(self, request, *args, **kwargs):
        try:





            offer_title = request.POST.get('OfferInput', '')
            print(offer_title)
            dil = request.POST.get('dil', '')
            print(dil)

            if offer_title != "":
                admin_id = zaptayadmin.objects.all().filter(email_id=request.session.get('admin_email_id')).first()
                offer_add = Offer(offer_title=offer_title, added_by=admin_id , is_active= False)
                offer_add.save()

            Offer_Choise = request.POST['OfferChoise']
            print(Offer_Choise )
            Prod_id = request.POST['prodid']
            print(Prod_id)
            offer_start = request.POST['start_date_time'].replace("T", " ")
            print(offer_start)
            offer_end = request.POST['end_date_time'].replace("T", " ")
            print(offer_end)
            Offer_Price = request.POST['OfferPrice']
            print(Offer_Price)

            if Offer_Choise != "" and Prod_id != "" and offer_start != "" and offer_end != "" and Offer_Price != "":
                admin_id = zaptayadmin.objects.all().filter(email_id=request.session.get('admin_email_id')).first()
                Offerid = Offer.objects.all().filter(offer_custom_id=Offer_Choise).first()
                Offerid.is_active = True

                prodid = Productmod.objects.all().get(prod_custom_id=Prod_id)
                prodid.Product_offer_start = offer_start
                prodid.Product_offer_end = offer_end
                prodid.extra_offer_price = Offer_Price
                prodid.Offer_Name = Offerid.offer_title

                offer_Product_add = OfferProduct(offer_id=Offerid,product_id=prodid,Product_offer_start=offer_start,Product_offer_end=offer_end,extra_offer_price=Offer_Price,added_by=admin_id)
                offer_Product_add.save()
                Offerid.save()
                prodid.save()
            else:
                print("blank")




            return redirect('admin_login:offer:OfferView')
        except Exception as e:
            print(e)
            return redirect('admin_login:offer:OfferView')


























# ******************************************************************************************************************
# Ajax hendel

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse


@csrf_exempt
def OfferDel(request):
    OfferID = request.POST['id']

    print()
    print()
    print('seller id :- ', OfferID)
    seller = Offer.objects.get(offer_custom_id=OfferID)
    seller.delete()

    print()
    print()
    print()

    podu = 'Done!'

    return JsonResponse({
        'prod': podu,
    })
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, TemplateView, FormView, ListView
from django.contrib import messages

from django.db.models import Subquery, Q
from .models import *


from admin_login.models import zaptayadmin
# Create your views here.
class Policy(TemplateView):

    template_name = 'admin_templates/admin_all_about_policy/policy.html'




    def post(self, request, *args, **kwargs):


        Product_Authentication_Policy = request.POST.get('Product_Authentication_Policy', '')
        print(Product_Authentication_Policy)
        if Product_Authentication_Policy != "":
            PAPDB = Product_Authentication_Policy_db(Product_Authentication_Policy_data=Product_Authentication_Policy)

            PAPDB.save()


        CashOnDeliveryPolicy = request.POST.get('CashOnDeliveryPolicy', '')
        print(CashOnDeliveryPolicy)
        if CashOnDeliveryPolicy != "":
            CODDB = CashOnDeliveryPolicy_db(CashOnDeliveryPolicy_data=str(CashOnDeliveryPolicy))

            CODDB.save()

        OnlinePaymentPolicy = request.POST.get('OnlinePaymentPolicy', '')
        print(OnlinePaymentPolicy)
        if OnlinePaymentPolicy != "":
            OPPDB = OnlinePaymentPolicy_db(OnlinePaymentPolicy_data=OnlinePaymentPolicy)
            print(OPPDB)
            OPPDB.save()

        FreeShippingPolicy = request.POST.get('FreeShippingPolicy', '')
        print(FreeShippingPolicy)
        if FreeShippingPolicy != "":
            FSPDB = FreeShippingPolicy_db(FreeShippingPolicy_data=FreeShippingPolicy)
            print(FSPDB)
            FSPDB.save()

        Return_Policy = request.POST.get('Return_Policy', '')
        print(Return_Policy)
        if Return_Policy != "":
            RPDB = Return_Policy_db(Return_Policy_data=Return_Policy)
            print(RPDB)
            RPDB.save()

        MembershipPolicy = request.POST.get('MembershipPolicy', '')
        print(MembershipPolicy)
        if MembershipPolicy != "":
            MPDB = MembershipPolicy_db(MembershipPolicy_data=MembershipPolicy)
            print(MPDB)
            MPDB.save()

        BestSeller = request.POST.get('BestSeller', '')
        print(BestSeller)
        if BestSeller != "":
            BSDB = BestSeller_db(BestSeller_data=BestSeller)
            print(BSDB)
            BSDB.save()

        SuperDeal = request.POST.get('SuperDeal', '')
        print(SuperDeal)
        if SuperDeal != "":
            SDDB = SuperDeal_db(SuperDeal_data=SuperDeal)
            print(SDDB)
            SDDB.save()

        MembershipZone = request.POST.get('MembershipZone', '')
        print(MembershipZone)
        if MembershipZone != "":
            MZDB = MembershipZone_db(MembershipZone_data=MembershipZone)
            print(MZDB)
            MZDB.save()

        EventCoupon = request.POST.get('EventCoupon', '')
        print(EventCoupon)
        if EventCoupon != "":
            ECDB = EventCoupon_db(EventCoupon_data=EventCoupon)
            print(ECDB)
            ECDB.save()

        SendGift = request.POST.get('SendGift', '')
        print(SendGift)
        if SendGift != "":
            SGDB = SendGift_db(SendGift_data=SendGift)
            print(SGDB)
            SGDB.save()

        TermsPolicy = request.POST.get('TermsPolicy', '')
        print(TermsPolicy)
        if TermsPolicy != "":
            TPDB = TermsPolicy_db(TermsPolicy_data=TermsPolicy)
            print(TPDB)
            TPDB.save()

        Privacy = request.POST.get('Privacy', '')
        print(Privacy)
        if Privacy != "":
            PDB = Privacy_db(Privacy_data=Privacy)
            print(PDB)
            PDB.save()

        ContactUs = request.POST.get('ContactUs', '')
        print(ContactUs)
        if ContactUs != "":
            CUDB = ContactUs_db(ContactUs_data=SuperDeal)
            print(CUDB)
            CUDB.save()




        return HttpResponseRedirect('/zaptay-admin-login/Policy/')

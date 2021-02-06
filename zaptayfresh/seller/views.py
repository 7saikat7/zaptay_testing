from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, TemplateView, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from admin_login.models import zaptayadmin
from django.db.models import Subquery, Q
from .seller_forms import SellerForm
from .models import Seller
from zap_product.models import *

# Create your views here.

################################################## View seller List / All seller #####################################################
class ViewSellerList(ListView):
    template_name = 'admin_templates/admin_all_seller_list_templates/all_seller_list.html'
    model = Seller

    def dispatch(self, request, *args, **kwargs):
        try:
            resp = request.session['admin_email_id']
            return super(ViewSellerList, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print( e)
            #return redirect('/site-admin/seller/all-seller/')
            return redirect('admin_login:admin_loginpage')

    def get_context_data(self, **kwargs):
        context = dict()
        get_name = zaptayadmin.objects.all().get(email_id=self.request.session['admin_email_id'])
        seller_details = Seller.objects.all().order_by('seller_id')



        seller_dict = dict()
        for sel in seller_details:
            prod = Productmod.objects.filter(Q(seller=sel) & Q(is_approved=0)).count()
            seller_dict[sel]=prod




        context = {
            "page_name": "add_seller",
            "admin_name": get_name.admin_f_name + " " + get_name.admin_f_name,
            'seller': seller_dict
        }
        return context


################################################  View a Perticular Seller ####################################################
class ViewSeller(TemplateView):
    template_name = 'admin_templates/admin_seller_templates/seller.html'
    model = Seller

    def dispatch(self, request, *args, **kwargs):
        try:
            resp = request.session['admin_email_id']
            return super(ViewSeller, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)
            # return redirect('/site-admin/seller/seller-view/')
            return redirect('admin_login:admin_loginpage')

    def get_context_data(self, **kwargs):
        context = dict()
        seller_id = self.kwargs.get('seller_id')
        get_name = zaptayadmin.objects.all().get(email_id=self.request.session['admin_email_id'])
        seller_details = Seller.objects.all().filter(seller_id=seller_id).first()
        context = {"page_name": "add_seller", "admin_name": get_name.admin_f_name+" "+get_name.admin_f_name, 'seller': seller_details}
        return context

####################################################### Edit Seller ################################################################

class EditSeller(FormView):
    form_class = SellerForm
    template_name = 'admin_templates/admin_seller_templates/seller_form.html'
    success_url = '/zaptay-admin-login/seller/all-seller/'

    def dispatch(self, request, *args, **kwargs):
        try:
            resp = request.session['admin_email_id']
            return super(EditSeller, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print('seller ediit excpt')
            print(e)
            # return redirect('/site-admin/seller/add-seller/')
            return redirect('admin_login:admin_loginpage')

    def get_context_data(self, **kwargs):
        seller_id = self.kwargs.get('seller_id')
        context = dict()
        get_name = zaptayadmin.objects.all().get(email_id=self.request.session['admin_email_id'])
        seller_details = Seller.objects.all().filter(seller_id__icontains=seller_id).first()
        edit_form = SellerForm(
            initial={
                'seller_Company_Name': seller_details.seller_CompanyName,
                'seller_name': seller_details.seller_name,
                'seller_email': seller_details.seller_email_id,
                'seller_phone_no': seller_details.seller_phone_no,
                'seller_address': seller_details.seller_address,
                'seller_specification': seller_details.seller_specification,
                'seller_gst_no': seller_details.seller_gst_no,
                'seller_aadhaar_no': seller_details.seller_aadhaar_no,
                'seller_voter_no': seller_details.seller_voter_no,
                'Seller_BankDetails': seller_details.Seller_BankDetails,
                'seller_Password': seller_details.seller_PWD
            })
        context = {"page_name": "add_seller", "admin_name": get_name.admin_f_name+" "+get_name.admin_f_name, 'form':edit_form, 'seller_data':seller_details}
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            seller_title = request.POST['seller_Company_Name']
            seller_name = request.POST['seller_name']
            seller_email = request.POST['seller_email']
            seller_phone_no = request.POST['seller_phone_no']
            seller_addres = request.POST['seller_address']
            seller_specification = request.POST['seller_specification']
            seller_gst_no = request.POST['seller_gst_no']
            seller_aadhaar_no = request.POST['seller_aadhaar_no']
            seller_voter_no = request.POST['seller_voter_no']

            seller_password = request.POST['seller_Password']
            Seller_BankDetails = request.POST['Seller_BankDetails']


            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()

            print(seller_title )
            print(seller_name)
            print(seller_email)
            print(seller_phone_no)
            print(seller_gst_no)
            print(seller_aadhaar_no)
            print(seller_voter_no)
            print(seller_password)
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()

            edit_seller_id = self.kwargs.get('seller_id').upper()
            seller_data = Seller.objects.get(seller_id=edit_seller_id)

            if 'seller_img' in request.FILES:
                SellerImage = request.FILES['seller_img']
            else:
                SellerImage = seller_data.SellerImage


            if 'aadhaar_img' in request.FILES:
                SellerAdhaarImage = request.FILES['aadhaar_img']
            else:
                SellerAdhaarImage = seller_data.SellerAdhaarImage


            if 'voter_img' in request.FILES:
                SellerVoterImage = request.FILES['voter_img']
            else:
                SellerVoterImage = seller_data.SellerVoterImage


            if 'gst_img' in request.FILES:
                SellerGstNoImage = request.FILES['gst_img']
            else:
                SellerGstNoImage = seller_data.SellerGstImage


            seller_data.seller_CompanyName = seller_title
            seller_data.seller_name=seller_name
            seller_data.seller_email_id=seller_email
            seller_data.seller_phone_no=seller_phone_no
            seller_data.seller_address=seller_addres
            seller_data.seller_specification=seller_specification
            seller_data.seller_gst_no=seller_gst_no
            seller_data.seller_aadhaar_no=seller_aadhaar_no
            seller_data.seller_voter_no = seller_voter_no

            seller_data.seller_PWD= seller_password
            seller_data.Seller_BankDetails=Seller_BankDetails
            seller_data.SellerImage=SellerImage
            seller_data.SellerAdhaarImage=SellerAdhaarImage
            seller_data.SellerVoterImage=SellerVoterImage
            seller_data.SellerGstImage=SellerGstNoImage

            seller_data.save()
            #messages.success(request, 'Seller update')
            print()
            print()
            print( )
            print()
            print()

            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        # context = self.get_context_data(task_form=form)
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)


######################################################### Add new Seller #########################################################


class AddSellerForm(FormView):
    form_class = SellerForm
    template_name = 'admin_templates/admin_seller_templates/seller_form.html'

    success_url = '/zaptay-admin-login/seller/all-seller/'

    def dispatch(self, request, *args, **kwargs):
        try:
            resp = request.session['admin_email_id']
            return super(AddSellerForm, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)

            return redirect('admin_login:admin_loginpage')

    def get_context_data(self, **kwargs):
        context = dict()
        get_name = zaptayadmin.objects.all().get(email_id=self.request.session['admin_email_id'])
        context = {"page_name": "add_seller", "admin_name": get_name.admin_f_name+" "+get_name.admin_f_name, 'form':self.form_class}
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            seller_title = request.POST['seller_Company_Name']
            seller_name = request.POST['seller_name']
            seller_email = request.POST['seller_email']
            seller_phone_no = request.POST['seller_phone_no']
            seller_addres = request.POST['seller_address']
            seller_specification = request.POST['seller_specification']
            seller_gst_no = request.POST['seller_gst_no']
            seller_aadhaar_no = request.POST['seller_aadhaar_no']
            seller_voter_no = request.POST['seller_voter_no']
            seller_password = request.POST['seller_Password']
            Seller_BankDetails = request.POST['Seller_BankDetails']



            if 'seller_img' in request.FILES:
                SellerImage = request.FILES['seller_img']
            else:
                SellerImage = ''

            if 'aadhaar_img' in request.FILES:
                SellerAdhaarImage = request.FILES['aadhaar_img']
            else:
                SellerAdhaarImage = ''

            if 'voter_img' in request.FILES:
                SellerVoterImage = request.FILES['voter_img']
            else:
                SellerVoterImage =  ''

            if 'gst_img' in request.FILES:
                SellerGstNoImage = request.FILES['gst_img']
            else:
                SellerGstNoImage =  ''
            print()
            print()
            print()
            print()
            print(seller_title)
            print()
            print(Seller_BankDetails)
            print(seller_password)
            print(SellerImage)
            print(SellerAdhaarImage)
            print(SellerVoterImage)
            print(SellerGstNoImage)
            print()
            print()
            print()
            print()
            print()


            admin_id = zaptayadmin.objects.all().get(email_id=request.session.get('admin_email_id'))
            seller_data = Seller(
                seller_CompanyName=seller_title,
                seller_name=seller_name,
                seller_email_id=seller_email,
                seller_phone_no=seller_phone_no,
                seller_address=seller_addres,
                seller_specification=seller_specification,
                seller_gst_no=seller_gst_no,
                seller_aadhaar_no=seller_aadhaar_no,
                seller_voter_no=seller_voter_no,
                added_by=admin_id,
                seller_PWD=seller_password,
                Seller_BankDetails=Seller_BankDetails,
                SellerImage=SellerImage,
                SellerAdhaarImage=SellerAdhaarImage,
                SellerVoterImage=SellerVoterImage,
                SellerGstImage=SellerGstNoImage,
            )
            print (seller_data)
            seller_data.save()
            print('seller created')
            #messages.success(request, 'Seller created')
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        # context = self.get_context_data(task_form=form)
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)



#########################################################   Seller Database #########################################################
class SellerDatabase(TemplateView):

    template_name = 'admin_templates/admin_seller_templates/seller_database.html'

    success_url = '/zaptay-admin-login/seller/all-seller/'

    def dispatch(self, request, *args, **kwargs):
        try:
            resp = request.session['admin_email_id']
            return super(SellerDatabase, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)

            return redirect('admin_login:admin_loginpage')

    def get_context_data(self, **kwargs):
        seller_id = self.kwargs.get('seller_id').upper()
        seller_details = Seller.objects.get(seller_id__icontains=seller_id)
        prodlist = Productmod.objects.filter(seller=seller_details)
        print()
        print()
        print()
        print(seller_details)
        print(seller_id)
        print(prodlist)
        print()
        print()
        context = dict()
        get_name = zaptayadmin.objects.all().get(email_id=self.request.session['admin_email_id'])
        context = {"page_name": "add_seller",
        "admin_name": get_name.admin_f_name + " " + get_name.admin_f_name,
        'seller': seller_details,
        'produ': prodlist

          }
        return context
#########################################################   Seller DashBoard #########################################################
class SellerDashBoard(TemplateView):

    template_name = 'admin_templates/admin_seller_templates/seller_dashboard.html'

    success_url = '/zaptay-admin-login/seller/all-seller/'

    def dispatch(self, request, *args, **kwargs):
        try:
            resp = request.session['admin_email_id']
            return super(SellerDashBoard,  self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)

            return redirect('admin_login:admin_loginpage')

    def get_context_data(self, **kwargs):
        seller_id = self.kwargs.get('seller_id').upper()
        seller_details = Seller.objects.get(seller_id__icontains=seller_id)
        prodlist = Productmod.objects.filter(Q(seller=seller_details))
        print()
        print()
        print()
        print(seller_details)
        print(seller_id)
        print(prodlist)
        print()
        print()
        context = dict()
        get_name = zaptayadmin.objects.all().get(email_id=self.request.session['admin_email_id'])
        context = {
            "page_name": "add_seller",
            "admin_name": get_name.admin_f_name + " " + get_name.admin_f_name,
            'seller': seller_details,
            'produ': prodlist
        }
        return context






# ******************************************************************************************************************
# Ajax hendel

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse


@csrf_exempt
def SellerDel(request):
    sellerID = request.POST['id']

    print()
    print()
    print('seller id :- ',  sellerID)
    seller = Seller.objects.get(seller_id=sellerID)
    seller.delete()


    print()
    print()
    print()

    podu = 'Done!'

    return JsonResponse({
        'prod': podu,
    })




@csrf_exempt
def SellerActivate(request):
    sellerID = request.POST['id']

    print()
    print()
    print('seller id :- ',  sellerID)
    seller = Seller.objects.get(seller_id=sellerID)
    seller.is_active = 1
    seller.save()
    prod = Productmod.objects.filter(seller=seller)
    for pro in prod:
        pro.is_approved = 1
        pro.save()



    print()
    print()
    print()

    podu = 'Done!'

    return JsonResponse({
        'prod': podu,
    })



@csrf_exempt
def SellerDeactivate(request):
    sellerID = request.POST['id']

    print()
    print()
    print('seller id :- ',  sellerID)
    seller = Seller.objects.get(seller_id=sellerID)

    seller.is_active = 0
    seller.save()
    prod = Productmod.objects.filter(seller=seller)
    for pro in prod:
        pro.is_approved = 0
        pro.save()




    print()
    print()
    print()

    podu = 'Done!'

    return JsonResponse({
        'prod': podu,
    })









@csrf_exempt
def ProductActivate(request):
    ProdID = request.POST['id']
 
    prod = Productmod.objects.get(prod_custom_id=ProdID)

    prod.is_approved = 1
    prod.save()
 
 
    podu = 'Done!'

    return JsonResponse({
        'prod': podu,
    })






@csrf_exempt
def ProductDeactivate(request):
    ProdID = request.POST['id']
 
    prod = Productmod.objects.get(prod_custom_id=ProdID)

    prod.is_approved = 0
    prod.save()
 
    podu = 'Done!'

    return JsonResponse({
        'prod': podu,
    })
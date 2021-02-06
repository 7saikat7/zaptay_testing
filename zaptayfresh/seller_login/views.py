from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import *

from .seller_login_forms import *
from .models import *

from django.core.mail import EmailMessage

from django.contrib.auth import logout

# ===================== Same Import From Zap Product For addProduct Form ===========================================
from django.contrib import messages
import os
from django.db.models import Subquery, Q
from zap_product.zap_product_form import *
from zap_product.models import *
import uuid
from attribute.models import *
from seller.models import *
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from admin_login.models import zaptayadmin
from seller_login.models import seller_login
import random
# ===================== Same Import From Zap Product For addProduct Form end ===========================================

# Create your views here.

########################################################## Seller Login ############################################################################


class ShowsellerLogin(FormView):
    form_class = LoginForm
    template_name = 'admin_templates/seller_login_Templates/seller_login.html'
    success_url = 'seller_dashboard'

    def post(self, request, *args, **kwargs):
        UloginForm = self.get_form()

        if UloginForm.is_valid():
            try:
                Uemail_id = UloginForm.cleaned_data['email_id']
                print(Uemail_id)  # print
                Upwd = UloginForm.cleaned_data['password']
                print(Upwd)

                session_data = Seller.objects.all().get(seller_email_id=Uemail_id,  seller_PWD=Upwd)
                print('session data variable')  # print
                print(session_data.seller_email_id)
                print(session_data.seller_PWD)

                #session set
                request.session['seller_email_id'] = session_data.seller_email_id
                request.session.set_expiry(0)
                print('session set done!')  # print

                return self.form_valid(UloginForm)
            except Exception as e:
                print(e)
                context = {"db_error": "User Not Exist", 'form': UloginForm}
                return self.render_to_response(context)
        else:
            return self.form_invalid(UloginForm)


############################################## Seller Dash Board ############################################################################
class SellerDashBoard(TemplateView):
    template_name = 'admin_templates/seller_login_Templates/sellerMenu.html'

    def dispatch(self, request, *args, **kwargs):

        try:
            resp = request.session['seller_email_id']
            if resp is None:
                print('session dose not matched for dashboard')  # print
            else:
                print('session matched for dashboard')  # print
            return super(SellerDashBoard, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)
            return redirect('seller_login:seller_loginpage')

    def get_context_data(self, **kwargs):

        get_name = Seller.objects.all().get(
            seller_email_id=self.request.session['seller_email_id'])
        context = dict()
        context = {
            "seller": get_name,
            
        }
        return context


###################################################### Seller Add Product #################################################################
class Aprod(FormView):
    form_class = ProductForm
    template_name = 'admin_templates/seller_login_Templates/seller_addProduct.html'
    success_url = '/zaptay-admin-login/product/product-form/'

    def dispatch(self, request, *args, **kwargs):

        try:
            resp = request.session['seller_email_id']
            if resp is None:
                print('session dose not matched for dashboard')  # print
            else:
                print('session matched for dashboard')  # print
            return super(Aprod, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)
            return redirect('seller_login:seller_loginpage')

    def get_context_data(self, **kwargs):

        context = dict()
        imgfrm = ProductImageForm()
        # get_name = zaptayadmin.objects.all().get( email_id=self.request.session['seller_email_id'])
        context = {
            'imgfrm': imgfrm,
            "page_name": "add_product",
            # "admin_name": get_name.admin_f_name + " " + get_name.admin_l_name,
            'form': self.form_class
        }
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        #getting main form data
        try:

            if 'product_title' in request.POST:
                product_titlee = request.POST['product_title']
                print(product_titlee)

            if 'category' in request.POST:
                Category = request.POST['category']
                caT_instance = MainCategory.objects.all().get(
                    category_id=Category)
                print(caT_instance)

            if 'sub_category' in request.POST:
                Sub_Category = request.POST['sub_category']
                Sub_caT_instance = SubCategory.objects.all().get(
                    sub_category_id=Sub_Category)
                print(Sub_caT_instance)

            if 'tertiary' in request.POST:
                Tertiary = request.POST['tertiary']
                Ter_instance = TertiaryCategory.objects.all().get(
                    ter_category_id=Tertiary)
                print(Ter_instance)

            if 'under_tertiary' in request.POST:
                Under_Tertiary = request.POST['under_tertiary']
                UnderT_instance = UnderTertiaryCategory.objects.all().get(
                    under_ter_category_id=Under_Tertiary)
                print(UnderT_instance)

            if 'seller' in request.POST:
                Selr = request.POST['seller']
                Selr_instance = Seller.objects.all().get(seller_id=Selr)
                print(Selr_instance)

            if 'made_in' in request.POST:
                Made_in = request.POST['made_in']
                Made_in_instance = MadeIn.objects.all().get(source_id=Made_in)
                print(Made_in_instance)

            if 'brand' in request.POST:
                Brand_in = request.POST['brand']
                Brand_instance = Brand.objects.all().get(brand_id=Brand_in)
                print(Brand_instance)

            if 'description' in request.POST:
                describtion = request.POST['description']
                print(describtion)

            if 'same_day_delivary_check' in request.POST:
                sameDayDel = True
                sameDayDelPrice = request.POST['same_day_delivary_price']
                print(sameDayDel)
                print('sane day delivery price' + sameDayDelPrice)
            else:
                sameDayDel = False
                sameDayDelPrice = 0.00

            if 'next_day_delivary_check' in request.POST:
                nxtDayDel = True
                nxtDayDelPrice = request.POST['next_day_delivary_price']
                print(nxtDayDel)
                print('next day delivery price ' + nxtDayDelPrice)
            else:
                nxtDayDel = False
                nxtDayDelPrice = 0.00

            if 'customize_delivary_check' in request.POST:
                custDel = True
                custDelDay = request.POST['customize_delivary_day']
                custDelPrice = request.POST['customize_delivary_price']
                print(custDelDay)
                print('Custom  delivery price ' + custDelPrice)
            else:
                custDel = False
                custDelDay = 0
                custDelPrice = 0.00

            if 'cod' in request.POST:
                cod = True
                print('cod')
                print(cod)
            else:
                cod = False

            Return = True
            print('Return ')
            print(Return)

            if 'AddToOffer' in request.POST:
                addToOffer = True
                print('add to offer:- ')
                print(addToOffer)
            else:
                addToOffer = False

            if 'B2b_check' in request.POST:
                b2b_check = True
                print('b2b')
                print(b2b_check)
            else:
                b2b_check = False

            if 'color' in request.POST:
                Color = request.POST['color']
                color_instance = Colour.objects.all().get(color_id=Color)
                print('color :- ')
                print(color_instance)

            if 'stock' in request.POST:
                Stock = request.POST['stock']
                print('stock :- ' + Stock)
                if Stock == '':
                    Stock = 0

            if 'product_image' in request.FILES:
                product_image_array = request.FILES.getlist('product_image')
                print(product_image_array)
                sl_no = request.POST.getlist('product_sl_image')
                print(sl_no)
                # is_home_image_select = request.POST.getlist('product_home_image')
                # print (is_home_image_select)
                i = 0
                imagefirst = ''
                secondimg = ''
                thirdimg = ''
                fourthimg = ''
                fifthimg = ''
                sixth = ''
                for product_image, sl_nunu in zip(product_image_array, sl_no):

                    if sl_nunu == '1':
                        imagefirst = product_image
                        print()
                        print('1')
                        print(imagefirst)
                        print()

                    if sl_nunu == '2':
                        secondimg = product_image
                        print()
                        print('2')
                        print(secondimg)
                        print()

                    if sl_nunu == '3':
                        thirdimg = product_image
                        print()
                        print('3')
                        print(thirdimg)
                        print()

                    if sl_nunu == '4':
                        fourthimg = product_image
                        print()
                        print('4')
                        print(fourthimg)
                        print()

                    if sl_nunu == '5':
                        fifthimg = product_image
                        print()
                        print('5')
                        print(fifthimg)
                        print()

                    if sl_nunu == '6':
                        sixth = product_image
                        print()
                        print('6')
                        print(sixth)
                        print()

                    i = i + 1

            if 'youtube' in request.POST:
                Utube = request.POST['youtube']
                print('YouTube :- ' + Utube)

            if 'main_price' in request.POST:
                mPrice = request.POST['main_price']
                print('main_price :- ' + mPrice)

            if 'offer_price' in request.POST:
                offerPrice = request.POST['offer_price']
                print('offer_price :- ' + offerPrice)

            if 'product_title' in request.POST:
                admin_id = zaptayadmin.objects.all().get(
                    email_id=request.session.get('admin_email_id'))
                print(admin_id)

                product_data = Productmod(
                    prod_title=product_titlee,
                    prod_category=caT_instance,
                    prod_sub_category=Sub_caT_instance,
                    prod_tertiary_category=Ter_instance,
                    prod_under_tertiary_category=UnderT_instance,
                    prod_brand=Brand_instance,
                    prod_made_in=Made_in_instance,
                    prod_desc=describtion,
                    seller=Selr_instance,
                    same_day_delivery=sameDayDel,
                    same_day_delivery_price=sameDayDelPrice,
                    next_day_delivery=nxtDayDel,
                    next_day_delivery_price=nxtDayDelPrice,
                    customize_day_delivery=custDel,
                    customize_day_delivery_day=custDelDay,
                    customize_day_delivery_price=custDelPrice,
                    product_return=Return,
                    cash_on_delivery=cod,
                    added_by=admin_id,
                    m_price=mPrice,
                    is_add2offer=addToOffer,
                    off_price=offerPrice,
                    is_b2b=b2b_check,
                    stock=Stock,
                    youtube_link=Utube,
                    prod_color=color_instance,
                    prod_image_id=uuid.uuid4(),
                    prod_track_id=uuid.uuid4(),
                    MCproduct='mother',
                    product_image1=imagefirst,
                    product_image2=secondimg,
                    product_image3=thirdimg,
                    product_image4=fourthimg,
                    product_image5=fifthimg,
                    product_image6=sixth,
                    sizetrack=uuid.uuid4(),
                    is_approved=0)
                product_data.save()

                if 'size' in request.POST:
                    Size = request.POST.getlist('size')

                    print(Size)
                    for s in Size:
                        print(s)
                        sizes = prodSize(
                            prodsize_id=uuid.uuid4(),
                            size_name=s,
                            trackidSize=product_data.sizetrack,
                            product=product_data,
                        )
                        sizes.save()

        except Exception as e:
            print('post exception main form')
            print(e)

        #Getting More Add Form Data
        try:

            if 'product_titlee' in request.POST:
                product_titleee = request.POST['product_titlee']
                print(product_titleee)

            if 'prod_idimg' in request.POST:
                Prod_id = request.POST['prod_idimg']
                # if Prod_id != '':
                #     Proddd_instance = Productmod.objects.all().get(prod_custom_id=Prod_id)

            if 'colorimg' in request.POST:
                Color = request.POST['colorimg']
                color_instanceimgs = Colour.objects.all().get(color_id=Color)
                print(color_instanceimgs)

            if 'stockimg' in request.POST:
                Stockimgs = request.POST['stockimg']
                print(Stockimgs)

            if 'youtubeimg' in request.POST:
                Utubeee = request.POST['youtubeimg']
                print(Utubeee)

            if 'main_priceimg' in request.POST:
                M_price = request.POST['main_priceimg']
                print(M_price)

            if 'sell_priceimg' in request.POST:
                S_price = request.POST['sell_priceimg']
                print(S_price)

            # if 'product_imageimg' in request.FILES:
            #     product_image_array = request.FILES.getlist('product_image')
            #     print(product_image_array)
            #     product_title = product_titlee
            #     for product_image in product_image_array:
            #         fs = FileSystemStorage()
            #         image_title = product_title + "." + product_image.name.split('.')[-1]
            #         image_title = image_title.replace(" ", "")
            #         upload_image = fs.save("products/images/" + image_title,
            #                                product_image)
            #         img_url = fs.url(upload_image)
            #         mod_image_name = img_url.split("/")[-1]
            #         image_path = 'products/images/' + mod_image_name

            if 'product_imageimg' in request.FILES:
                Proddd_instance = Productmod.objects.all().get(
                    prod_custom_id=Prod_id)
                product_image_array = request.FILES.getlist('product_imageimg')
                print(product_image_array)
                sl_no = request.POST.getlist('product_sl_image')
                print(sl_no)
                # is_home_image_select = request.POST.getlist('product_home_image')
                # print (is_home_image_select)
                i = 0
                imagefirst = ''
                secondimg = ''
                thirdimg = ''
                fourthimg = ''
                fifthimg = ''

                sixthimg = ''
                for product_image, sl_nunu in zip(product_image_array, sl_no):
                    if sl_nunu == '1':
                        imagefirst = product_image
                        print()
                        print('1')
                        print(imagefirst)
                        print()

                    if sl_nunu == '2':
                        secondimg = product_image
                        print()
                        print('2')
                        print(secondimg)
                        print()

                    if sl_nunu == '3':
                        thirdimg = product_image
                        print()
                        print('3')
                        print(thirdimg)
                        print()

                    if sl_nunu == '4':
                        fourthimg = product_image
                        print()
                        print('4')
                        print(fourthimg)
                        print()

                    if sl_nunu == '5':
                        fifthimg = product_image
                        print()
                        print('5')
                        print(fifthimg)
                        print()

                    if sl_nunu == '6':
                        sixthimg = product_image
                        print()
                        print('6')
                        print(sixthimg)
                        print()

                    i = i + 1

            if 'prod_idimg' in request.POST:
                prod_instance = Productmod.objects.all().get(
                    prod_custom_id=Prod_id)
                product_datachild = Productmod(
                    prod_title=product_titleee,
                    prod_category=prod_instance.prod_category,
                    prod_sub_category=prod_instance.prod_sub_category,
                    prod_tertiary_category=prod_instance.
                    prod_tertiary_category,
                    prod_under_tertiary_category=prod_instance.
                    prod_under_tertiary_category,
                    prod_brand=prod_instance.prod_brand,
                    prod_made_in=prod_instance.prod_made_in,
                    prod_desc=prod_instance.prod_desc,
                    seller=prod_instance.seller,
                    same_day_delivery=prod_instance.same_day_delivery,
                    same_day_delivery_price=prod_instance.
                    same_day_delivery_price,
                    next_day_delivery=prod_instance.next_day_delivery,
                    next_day_delivery_price=prod_instance.
                    next_day_delivery_price,
                    customize_day_delivery=prod_instance.
                    customize_day_delivery,
                    customize_day_delivery_day=prod_instance.
                    customize_day_delivery_day,
                    customize_day_delivery_price=prod_instance.
                    customize_day_delivery_price,
                    product_return=prod_instance.product_return,
                    cash_on_delivery=prod_instance.cash_on_delivery,
                    added_by=prod_instance.added_by,
                    m_price=M_price,
                    is_add2offer=prod_instance.is_add2offer,
                    off_price=prod_instance.off_price,
                    is_b2b=prod_instance.is_b2b,
                    stock=Stockimgs,
                    youtube_link=Utubeee,
                    prod_color=color_instanceimgs,
                    prod_image_id=uuid.uuid4(),
                    prod_track_id=prod_instance.prod_track_id,
                    MCproduct='child',
                    product_image1=imagefirst,
                    product_image2=secondimg,
                    product_image3=thirdimg,
                    product_image4=fourthimg,
                    product_image5=fifthimg,
                    product_image6=sixthimg,
                    sizetrack=uuid.uuid4(),
                    is_approved=0)
                product_datachild.save()

                if 'sizeimg' in request.POST:
                    Size = request.POST.getlist('sizeimg')

                    print(Size)
                    for s in Size:
                        print(s)
                        sizes = prodSize(
                            prodsize_id=uuid.uuid4(),
                            size_name=s,
                            trackidSize=product_datachild.sizetrack,
                            product=product_datachild,
                        )
                        sizes.save()

        except Exception as e:
            print('post exception')
            print(e)

        context = self.get_context_data()
        context['form'] = form
        if 'product_title' in request.POST:
            context['prodid'] = product_data.prod_custom_id
            context['prodimg'] = product_data.product_image

        if 'product_titlee' in request.POST:
            context['prodid'] = product_datachild.prod_custom_id

        return self.render_to_response(context)


###################################################### Seller Add Product  End #################################################################












# ---------------------------------------------------------- X X --------------------------------------------------------------















###################################################### Seller Dash #################################################################
class SellerDash(TemplateView):
    template_name = 'admin_templates/seller_login_Templates/seller_Dash.html'

    def dispatch(self, request, *args, **kwargs):

        try:
            resp = request.session['seller_email_id']
            if resp is None:
                print('session dose not matched for dashboard')  # print
            else:
                print('session matched for dashboard')  # print
            return super(SellerDash, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)
            return redirect('seller_login:seller_loginpage')

    def get_context_data(self, **kwargs):

        get_name = Seller.objects.all().get(seller_email_id=self.request.session['seller_email_id'])
        prod = Productmod.objects.filter(seller=get_name)
        context = dict()
        context = {
            "admin_name": get_name.seller_email_id,
            'seller': get_name,
            'produ': prod
        }
        return context


###################################################### Seller Dash End #################################################################













# ---------------------------------------------------------- X X --------------------------------------------------------------









###################################################### Seller orderList #################################################################
class orderListWaiting(TemplateView):
    template_name = 'admin_templates/seller_login_Templates/Seller_orderList.html'

    def dispatch(self, request, *args, **kwargs):

        try:
            resp = request.session['seller_email_id']
            if resp is None:
                print('session dose not matched for dashboard')  # print
            else:
                print('session matched for dashboard')  # print
            return super(orderListWaiting, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)
            return redirect('seller_login:seller_loginpage')

    def get_context_data(self, **kwargs):

        get_name = seller_login.objects.all().get(
            email_id=self.request.session['seller_email_id'])
        context = dict()
        context = {
            "page_name": "dashboard",
            "admin_name": get_name.seller_f_name + " " + get_name.seller_l_name
        }
        return context




class orderListSold(TemplateView):
    template_name = 'admin_templates/seller_login_Templates/seller_orderSoldList.html'

    def dispatch(self, request, *args, **kwargs):

        try:
            resp = request.session['seller_email_id']
            if resp is None:
                print('session dose not matched for dashboard')  # print
            else:
                print('session matched for dashboard')  # print
            return super(orderListSold, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)
            return redirect('seller_login:seller_loginpage')

    def get_context_data(self, **kwargs):

        get_name = seller_login.objects.all().get(
            email_id=self.request.session['seller_email_id'])
        context = dict()
        context = {
            "page_name": "dashboard",
            "admin_name": get_name.seller_f_name + " " + get_name.seller_l_name
        }
        return context


###################################################### Seller orderList End #################################################################







# ---------------------------------------------------------- X X --------------------------------------------------------------





###################################################### Seller SellerReturn #################################################################
class SellerReturn(TemplateView):
    template_name = 'admin_templates/seller_login_Templates/SellerReturn.html'

    def dispatch(self, request, *args, **kwargs):

        try:
            resp = request.session['seller_email_id']
            if resp is None:
                print('session dose not matched for dashboard')  # print
            else:
                print('session matched for dashboard')  # print
            return super(SellerReturn, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)
            return redirect('seller_login:seller_loginpage')

    def get_context_data(self, **kwargs):

        get_name = seller_login.objects.all().get(
            email_id=self.request.session['seller_email_id'])
        context = dict()
        context = {
            "page_name": "dashboard",
            "admin_name": get_name.seller_f_name + " " + get_name.seller_l_name
        }
        return context


###################################################### Seller SellerReturn End #################################################################










# ---------------------------------------------------------- X X --------------------------------------------------------------













###################################################### Seller Log Out #################################################################


def Logout(request):
    logout(request)
    return redirect('seller_login:seller_loginpage')


################################################ Seller Forget Password section  #######################################################



















# ########################### Un Used View ############################################
class ResetPwd(FormView):
    form_class = ResetPwd
    # template_name = 'admin_templates/admin_login_Templates/reset_password.html'
    success_url = '/seller-admin-login/ResetPwd/'

    def post(self, request, *args, **kwargs):
        resetFrm = self.get_form()

        if resetFrm.is_valid():
            try:
                Uemail_id = resetFrm.cleaned_data['email_id_forReset']
                print(Uemail_id)  # print

                em = seller_login.objects.all().get(email_id=Uemail_id)
                if em != ' ':
                    email = EmailMessage(
                        subject='Hello this is a test mail',
                        body='Body goes here .............................',
                        from_email='admin@zaptay.com',
                        to=[Uemail_id],
                        reply_to=[Uemail_id],
                        headers={'Content-Type': 'text/plain'},
                    )
                    email.send()

                return self.form_valid(resetFrm)
            except Exception as e:
                print('excpt')
                print(e)
                context = {"db_error": "User Not Exist", 'form': resetFrm}
                return self.render_to_response(context)


#+++++++++++++++++++++++++++++++++++++++++++++ Password Change Form ++++++++++++++++++++++++++++
class PwdChangeFrm(FormView):
    form_class = ResetPwd
    # template_name = 'admin_templates/admin_login_Templates/reset_password.html'
    success_url = '/seller-admin-login/ResetPwd/'

    def post(self, request, *args, **kwargs):
        resetFrm = self.get_form()

        if resetFrm.is_valid():
            try:
                Uemail_id = resetFrm.cleaned_data['email_id_forReset']
                print(Uemail_id)  # print

                em = seller_login.objects.all().get(email_id=Uemail_id)
                if em != ' ':
                    email = EmailMessage(
                        subject='Hello this is a test mail',
                        body='Body goes here .............................',
                        from_email='admin@zaptay.com',
                        to=[Uemail_id],
                        reply_to=[Uemail_id],
                        headers={'Content-Type': 'text/plain'},
                    )
                    email.send()

                return self.form_valid(resetFrm)
            except Exception as e:
                print('excpt')
                print(e)
                context = {"db_error": "User Not Exist", 'form': resetFrm}
                return self.render_to_response(context)

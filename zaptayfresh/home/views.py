from django.shortcuts import *
from django.views.generic import *
from django.shortcuts import render,redirect
from django.db.models import Subquery
from django.contrib import messages
from django.db import IntegrityError
from pymongo.errors import BulkWriteError
from django.contrib.auth.models import User,auth
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from .forms import RegistrationForm
from django.views.generic import View, TemplateView, FormView
from django.db.utils import DatabaseError
from .userlogin_forms import LoginForm , ResetPwd
from .models import zaptayuser
from django.urls import reverse
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.template.loader import render_to_string
#from .token_generator import account_activation_token
from home.utils import account_activation_token
from django.core.mail import EmailMessage ,send_mail
from django.contrib.sites.shortcuts import get_current_site

from django.contrib.auth import logout,login
from django.http import JsonResponse

from banner.models import *
from offer.models import *
from attribute.models import *
from zap_product.models import *
# from stock.models import Bach, Inventory
# from offer.models import Offer, OfferProduct
#from user_login.models import UserAccount

from django.utils import timezone
from datetime import datetime
from django.db.models import Subquery , Q
from . base_template import BaseTemplateHeader

# Create your views here.
################################## SIGNUP #######################################
# class ShowuserSignup(FormView):

def ShowuserSignup(request):
    
       
    if request.method =='POST':
            username = request.POST['fname']
            print(username)
            
            password = request.POST['pwd']
            password2 = request.POST['pwd2']
            # phone_no = request.POST['pno']
            # print(phone_no)
            email = request.POST['email']
            print(email)
            if password == password2:
                try:
                    user = User.objects.create_user(username=username, email=email, password=password
                    )
                    user.is_active=False
                    user.save()
                    
                    uidb64=urlsafe_base64_encode(force_bytes(user.pk))
                    domain=get_current_site(request).domain
                    link=reverse('home:activate',kwargs={'uidb64':uidb64,'token':account_activation_token.make_token(user)})
                    activate_url='http://'+domain+link #########must be https
                    email_subject='THE MAIL'
                    email_body='Hi'+ user.username +'user this link to verify your account\n'+activate_url
                    email=EmailMessage(
                    
                            email_subject,
                            email_body,
                            
                            'noreply@example.com',
                            [email],
                           
                        )
                    email.send()
                    print("got upto this ")
                    
                    print('email send')
                   
                    contex={'A':'Thanks For Registration Please confirm your account activation mail and also check in sapm for mail'}
                    #return redirect('/user_login/',foo='bara bara')
                    return render(request,'user_templates/user_login/user_signup.html',contex)
                except DatabaseError:
                    print('django mongo bd database error ---------------------')
                    return render(request,'user_templates/user_login/user_signup.html',{'error': "Username Is Already Taken  Let's Something else "})
                except IntegrityError:
                    return render(request,'user_templates/user_login/user_signup.html',{'error2': "Username Is Already Taken , Let's Try Something else "})
            
            
            else:                 
                 return render(request,'user_templates/user_login/user_signup.html',{'not_match':'Password do not match'})     
    else:
        return render(request,'user_templates/user_login/user_signup.html')
class Verificationview(View):
  def get(self,request,uidb64,token):
        print('activated succesfully +++++++++++++++++++++++++++++++')
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
            if user.is_active :
                 return redirect('/ShowuserLogin/')
            user.is_active=True
            user.save()
            messages.success(request,'Account activated')
            return redirect('/ShowuserLogin/')

        except Exception as identifier:
            user = None
            if user is not None and account_activation_token.check_token(user, token):
                user.is_active = True
                user.save()
                return redirect('/ShowuserLogin/')
                # return HttpResponse('Activation link is invalid!')
                #return redirect('/ShowuserLogin/')
            else:
              return render(request,'user_templates/user_login/failauth.html')



# def mail_activation(request,uid64,token):
#     try:
#         uid=urlsafe_base64_decode(uid64).decode()
#         user=User._default_manager.get(pk=uid)
#     except(TypeError,ValueError,OverflowError,User.DoesNotExist):
#         user=None
#     if user is not None and account_activation_token.check_token(user,token):
#         user.is_active =True
#         user.save()
#         messages.success(request,'your account is active')
#         return redirect('ShowuserLoginlogin')
#     else:
#         messages.warning(request,'Invalid Activation Link')
#         return redirect('ShowuserLogin')
    # template_name = 'user_templates/user_login/user_signup.html'


    # def get_context_data(self, **kwargs):

    #     banners_head = webLogo.objects.filter(banner_name='weblogo').first()

    #     context = {
    #         'baner_head': banners_head,
    #     }
    #     return context


    # def post(self, request, *args, **kwargs):

    #     print()
    #     print()
    #     print()
    #     print()
    #     print()
    #     User_name = request.POST['fname']

    #     print(User_name)# print
    #     User_email = request.POST['uemail']

    #     print(User_email)
    #     User_phone = request.POST['pno']

    #     print(User_phone)
    #     User_password = request.POST['pwd']
    #     print(User_password)

    #     session_data = zaptayuser(user_name=User_name,
    #                                              email_id=User_email,
    #                                              password=User_password,
    #                                              phone_no=User_phone)
    #     session_data.save()


    #     print()
    #     print()
    #     print()
    #     print()
    #     context = {"db_error": "User Created!"}
    #     return self.render_to_response(context)





################################## LOGIN ########################################
def ShowuserLogin(request):
    
    if request.method == 'POST':
        print("post request is working ")
        USERNAME = request.POST['usermail']
        PASSWORD = request.POST['userword']
        x =auth.authenticate(request,username=USERNAME, password=PASSWORD)
       
        if x is not None:
                print("authenticated succesfull")
                login(request,x)
                print('succesfully ..............')
                return redirect('/')
        else:
                print("Not authenticating")
                contex2={'error4':"Invalid Username or Password"}
                return render(request,'user_templates/user_login/user_login.html',contex2)

    else:
       return render(request,'user_templates/user_login/user_login.html')
######################### logout ##################3

def user_Logout(request):
    logout(request)
    return redirect('/')


################################################ Forget Password section  #######################################################

class ResetPwd(FormView):
    form_class = ResetPwd
    template_name = 'admin_templates/admin_login_Templates/reset_password.html'
    success_url = '/zaptay-admin-login/ResetPwd/'

    def post(self, request, *args, **kwargs):
        resetFrm = self.get_form()

        if resetFrm.is_valid():
            try:
                Uemail_id = resetFrm.cleaned_data['email_id_forReset']
                print(Uemail_id)  # print

                em = zaptayadmin.objects.all().get(email_id=Uemail_id)
                if em != ' ' :
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
    template_name = 'admin_templates/admin_login_Templates/reset_password.html'
    success_url = '/zaptay-admin-login/ResetPwd/'

    def post(self, request, *args, **kwargs):
        resetFrm = self.get_form()

        if resetFrm.is_valid():
            try:
                Uemail_id = resetFrm.cleaned_data['email_id_forReset']
                print(Uemail_id)  # print

                em = zaptayadmin.objects.all().get(email_id=Uemail_id)
                if em != ' ' :
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


################################################# Usd ###########################
class MainHome(TemplateView):
    template_name = "user_templates/Home_user.html"

    def get_context_data(self, **kwargs):
        # ================================== get  Offer slider data =========================================
        Offers_all = Offer.objects.all()
        produ = Productmod.objects.filter(Q(is_approved=1))
        # print()
        # print()
        # print()
        # print()
        # print()
        offer_dict = dict()
        alloffer_dict = list()
        for i in Offers_all:
            offerprod =  Productmod.objects.filter(Q(Offer_Name= i) & Q(is_approved=1))[:12]
            offer_dict[i] = offerprod
            # offer_dict[i.offer_title]= offerprod

        # print('hi')
        # for intu in offer_dict:
        #     print(intu)
        #     print(offer_dict[intu])
        #     for pod in offer_dict[intu]:
        #         print(pod)

        # print()
        # print()
        # print()
        # print()
        # ================================== get  Offer slider data end =========================================




        subCat = SubCategory.objects.all()
        terCat = TertiaryCategory.objects.all()
        banners_head = webLogo.objects.filter(banner_name='weblogo').first()
        print('hi')
        print('hi')
        print('hi')
        print('hi')
        print('hi')
        print('hi')
        print('hi')
        print('hi')
        # print(banners_head.banner_image)
        print('hi')
        print('hi')
        print('hi')
        print('hi')
        print('hi')
        print('hi')
        print('hi')
        print('hi')


        # ====================================== Get feature category data ================================
        getFeatureSubCat = SubCategory.objects.all()
        getFeatureTerCat = TertiaryCategory.objects.all()
        # ====================================== Get feature category data end ================================




        # ============================== getting subcategory product slider data ==================================
        try:
            category_instance = MainCategory.objects.get(main_category_name__iexact="featured")
            subcategory = SubCategory.objects.filter(category_id_id=category_instance)
            print()
            print()
            print('hi', category_instance)
            print('sabu :- ',subcategory)
            subCatSlider = dict()
            for sab in subcategory:
                print(sab.sub_category_name)
                getting_prod = Productmod.objects.filter(Q(prod_sub_category=sab) & Q(is_approved=1))[:12]
                print(getting_prod)
                subCatSlider[sab] = getting_prod

            print()
            print()
            print()
            print('subcatslider data',subCatSlider)
            print()
            print()
        except Exception as e:
            print('getting subcategory product slider data Error  :- ',e)
            subCatSlider = dict()
        # ============================== getting subcategory product slider data end ==================================



        context = {
            'offers': offer_dict,
            'product': produ,
            'Subcat': subCat,
            'Tercat': terCat,
            'baner_head': banners_head,
            'featureSub': getFeatureSubCat,
            'featureter': getFeatureTerCat,
            'subcatsliderdata': subCatSlider
        }
        return context




class singleProduct(TemplateView):
    template_name = "user_templates/productView/productview.html"

    def get_context_data(self, **kwargs):
        Offers_all = Offer.objects.all()

        #################Product Data Get##########################
        productId = self.kwargs.get('Product_iD').upper()



        print(productId)
        produ = Productmod.objects.get(Q(prod_custom_id=productId) & Q(is_approved=1))
        colorprod = Productmod.objects.filter(Q(prod_track_id=produ.prod_track_id )& Q(is_approved=1))
        get_size = prodSize.objects.filter(trackidSize=produ.sizetrack)
        producti = Productmod.objects.filter(Q(is_approved=1))[0:12] #used for printing related product etc..






        subCat = SubCategory.objects.all()
        terCat = TertiaryCategory.objects.all()
        banners_head = webLogo.objects.filter(banner_name='weblogo').first()



        context = {
            'offers': Offers_all,
            'product': produ,
            'producti': producti,
            'color': colorprod,
            'Subcat': subCat,
            'Tercat': terCat,
            'baner_head': banners_head,
            'siz': get_size
        }
        return context


class SubCategoryProductView(TemplateView):
    template_name = "user_templates/subcategory/subcategory.html"

    def get_context_data(self, **kwargs):

        producti = Productmod.objects.filter(Q(is_approved=1))[0:12]
        subCat = SubCategory.objects.all()
        terCat = TertiaryCategory.objects.all()
        banners_head = webLogo.objects.filter(banner_name='weblogo').first()
        #################Product Data Get##########################

        # Getting clicked sub category
        subCatID = self.kwargs.get('sucat_id')
        ClickSubCat = SubCategory.objects.get(sub_category_id=subCatID)
        print(ClickSubCat)

        #Getting Banner Images of clicked sub category
        banu = Banner.objects.filter( banner_name=str(ClickSubCat.sub_category_name)).values('banner_image', 'banner_link', 'banner_id', 'banner_name')

        # getting tertiary category under clicked sub category
        Ter_cate = TertiaryCategory.objects.filter(sub_category_id=ClickSubCat)


        # getting subcat related product
        relatedProduct = Productmod.objects.filter(Q(prod_sub_category= ClickSubCat) & Q(is_approved=1))[0:12]


        #getting all data for filter section
        brand = Brand.objects.all()
        color = Colour.objects.all()
        size = Size.objects.all()





        context = {
            'producti': producti,
            'Subcat': subCat,
            'Tercat': terCat,
            'baner_head': banners_head,
            # this page datta
            'CurrentSubCat': ClickSubCat,
            'banu': banu,
            'Tercate': Ter_cate,
            'brand': brand,
            'col': color,
            'siz': size,
            'RP':relatedProduct
        }
        return context


class IndianHatt(TemplateView):
    template_name = "user_templates/inidan-hatt/inidanhatt.html"

    def get_context_data(self, **kwargs):
        Offers_all = Offer.objects.all()
        produ = Productmod.objects.filter( Q(is_approved=1))



        subCat = SubCategory.objects.all()
        terCat = TertiaryCategory.objects.all()
        # print(Offers_all)
        # print(subCat)
        # print(terCat)
        # for i in terCat:
        #     print(i.sub_category_id.sub_category_name)
        banners_head = webLogo.objects.filter(banner_name='weblogo').first()


        # ***************************************************************************************************************
        # *****************************  Featured Category content start  ****************************************************
        # ***************************************************************************************************************
        get_category = MainCategory.objects.filter(main_category_name='featured').first()
        get_sub_category = SubCategory.objects.filter(category_id=get_category)
        featured_category = list()
        for sub_category in get_sub_category:
            featured_category_dict = dict()
            get_tertitory_category = TertiaryCategory.objects.filter(sub_category_id=sub_category)
            featured_category_dict['sub_category'] = sub_category.sub_category_name
            featured_tertiary_category = list()
            for tertiary_category in  get_tertitory_category:
                featured_tertiary_category_dict = dict()
                featured_tertiary_category_dict['category_name'] = tertiary_category.ter_category_name
                featured_tertiary_category_dict['category_url'] = tertiary_category.ter_category_seo_url
                featured_tertiary_category_dict['category_image'] = tertiary_category.tertiary_category_image
                featured_tertiary_category.append(featured_tertiary_category_dict)
            featured_category_dict['tertiary_category'] = featured_tertiary_category
            featured_category.append(featured_category_dict)
        # print (featured_category)
        # *****************************  Featured Category content start  ****************************************************

        context = {
            'offers': Offers_all,
            'product': produ,

            'Subcat': subCat,
            'Tercat': terCat,
            'baner_head': banners_head,
            'featured_category': featured_category
        }
        return context


class b2b(TemplateView):
    template_name = "user_templates/b2b/b2b.html"

    def get_context_data(self, **kwargs):
        Offers_all = Offer.objects.all()[0:1]
        produ = Productmod.objects.filter( Q(is_approved=1))



        subCat = SubCategory.objects.all()
        terCat = TertiaryCategory.objects.all()
        # print(Offers_all)
        # print(subCat)
        # print(terCat)
        # for i in terCat:
        #     print(i.sub_category_id.sub_category_name)
        banners_head = webLogo.objects.filter(banner_name='weblogo').first()


        # ***************************************************************************************************************
        # *****************************  Featured Category content start  ****************************************************
        # ***************************************************************************************************************
        getFeatureSubCat = SubCategory.objects.all()
        getFeatureTerCat = TertiaryCategory.objects.all()
        # print (featured_category)
        # *****************************  Featured Category content start  ****************************************************

        context = {
            'offers': Offers_all,
            'product': produ,
            'Subcat': subCat,
            'Tercat': terCat,
            'baner_head': banners_head,
            'featureSub': getFeatureSubCat,
            'featureter': getFeatureTerCat
        }
        return context






class viewall(TemplateView):
    template_name = 'user_templates/viewall.html'

    def get_context_data(self, **kwargs):

        produ = Productmod.objects.filter( Q(is_approved=1))
        context = super().get_context_data(**kwargs)
        print()
        print()
        print()
        offerName = self.kwargs.get('name')
        off_instance = Offer.objects.get(offer_custom_id=offerName)
        products = Productmod.objects.filter(Q(Offer_Name=off_instance.offer_title) & Q(is_approved=1))[:12]

        print(self.kwargs.get('name'))

        print( )
        print()


        subCat = SubCategory.objects.all()
        terCat = TertiaryCategory.objects.all()
        # print(Offers_all)
        # print(subCat)
        # print(terCat)
        # for i in terCat:
        #     print(i.sub_category_id.sub_category_name)
        banners_head = webLogo.objects.filter(banner_name='weblogo').first()
        color = Colour.objects.all()




        context = {
            'offers': products,
            'product': produ,
            'Subcat': subCat,
            'Tercat': terCat,
            'baner_head': banners_head,

            'offerDetails': off_instance,
            'col': color


        }
        return context




class viewallSubCategory(TemplateView):
    template_name = 'user_templates/viewall-SubCategory.html'

    def get_context_data(self, **kwargs):

        produ = Productmod.objects.filter( Q(is_approved=1))
        context = super().get_context_data(**kwargs)
        print()
        print()
        print()
        sucatid = self.kwargs.get('name')
        Sucat_instance = SubCategory.objects.get(sub_category_id=sucatid)
        products = Productmod.objects.filter(Q(prod_sub_category=Sucat_instance) & Q(is_approved=1) )[:12]

        print(self.kwargs.get('name'))

        print(Sucat_instance)
        print(products)
        print( )
        print()


        subCat = SubCategory.objects.all()
        terCat = TertiaryCategory.objects.all()
        # print(Offers_all)
        # print(subCat)
        # print(terCat)
        # for i in terCat:
        #     print(i.sub_category_id.sub_category_name)
        banners_head = webLogo.objects.filter(banner_name='weblogo').first()

        color = Colour.objects.all()


        context = {
            'Subcatu': products,
            'product': produ,
            'Subcat': subCat,
            'Tercat': terCat,
            'baner_head': banners_head,
            'SucatDetails': Sucat_instance,
            'col': color
        }
        return context
# *************************************** Handeling cart *******************************
import json 
import requests

def cart(request):
    return render(request,'user_templates/productView/cart.html')

def updateItem(request):

        data = json.loads(request.body)
        productId = data['productId']
        action = data['action']
        print('Action:', action)
        print('Product:', productId)

        customer = request.user
        product = Productmod.objects.get(id=productId)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

        if action == 'add':
            orderItem.quantity = (orderItem.quantity + 1)
        elif action == 'remove':
            orderItem.quantity = (orderItem.quantity - 1)

            orderItem.save()
            if orderItem.quantity == 0:
                orderItem.delete()

        return JsonResponse('Item was added', safe=False)

    # # data=requests.body.decode('utf-8')
    # # receice_data=json.loads(data)
   
    # # print(receice_data)
    # task=json.loads(request.body)

    
   
    # print('it is printing it so the problem is not here ')
    # Productid=data['productId']
    # Action=data['action']
    # print(Productid)
    # # print('Productid:',Productid)
    # # print('Action:',Action)

    # customer = request.user
    # product=Productmod.objects.get(id=Productid)
    # order,created =Productmod.objects.get_or_create(customer=customer)
    # orderItem ,created =Productid.objects.get_or_create(order=order,product=product) ## glitch point 

    # return JsonResponse('item was added to cart ', safe=False)

# ******************************************************************************************************************
# Ajax hendel

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


# =========================================== Home Page =======================================
class bannerJasonList(View):
    def get(self, *args, **kwargs):
        baner = list(Banner.objects.values())
        return JsonResponse({'banerdata':baner})


@csrf_exempt
def bannerJasonListspecific(request):

    bannerName = request.POST['banname']
    print(bannerName)
    banu = Banner.objects.filter(banner_name=str(bannerName)).values( 'banner_image', 'banner_link', 'banner_id', 'banner_name')
    print(banu)
    baner = list(banu)
    return JsonResponse({'banerdata': baner})





# =========================================== Home Page end =======================================


# =============================== Sub Category PAge =====================================================
class underTerAll(View):
    def get(self, *args, **kwargs):
        underTer = list(UnderTertiaryCategory.objects.values())
        return JsonResponse({'UndTer':underTer})

@csrf_exempt
def underTerspecific(request):

    terID = request.POST['id']
    print(terID)
    tercat = TertiaryCategory.objects.get(ter_category_id=terID)
    print('tertiacry category : ', tercat)
    undTer = UnderTertiaryCategory.objects.filter(ter_category_id=tercat).values()
    print('UnderTer Category : ', undTer)
    # print(banu)
    undt = list(undTer)
    return JsonResponse({'underTer': undt})

@csrf_exempt
def allproduct(request):
    subvisibleprod = request.POST['visible']
    upper = int(subvisibleprod)
    lower = upper - 12

    subID = request.POST['id']
    ClickSubCat = SubCategory.objects.get(sub_category_id=subID)
    print('ajax clicked subcat :-', ClickSubCat)
    getprod = Productmod.objects.filter(Q(prod_sub_category=ClickSubCat) & Q(is_approved=1)).values()[lower:upper]
    undt = list(getprod)
    return JsonResponse({'prod': undt})



@csrf_exempt
def getprodbyBrand(request):
    subvisibleprod = request.POST['visible']
    upper = int(subvisibleprod)
    lower = upper - 12

    subID = request.POST['id']
    Bname = request.POST['brand']
    B_instance = Brand.objects.get(brand_id=Bname)
    ClickSubCat = SubCategory.objects.get(sub_category_id=subID)
    print('ajax clicked subcat :-', ClickSubCat)
    getprod = Productmod.objects.filter(Q(prod_sub_category=ClickSubCat) & Q(prod_brand=B_instance) & Q(is_approved=1)).values()[lower:upper]
    undt = list(getprod)
    return JsonResponse({'prod': undt})

@csrf_exempt
def getprodbycolor(request):
    subvisibleprod = request.POST['visible']
    upper = int(subvisibleprod)
    lower = upper - 12

    subID = request.POST['id']
    Cname = request.POST['col']
    C_instance = Colour.objects.get(color_id=Cname)
    ClickSubCat = SubCategory.objects.get(sub_category_id=subID)
    print('ajax clicked subcat :-', ClickSubCat)
    getprod = Productmod.objects.filter(Q(prod_sub_category=ClickSubCat) & Q(prod_color=C_instance) & Q(is_approved=1)).values()[lower:upper]
    undt = list(getprod)
    return JsonResponse({'prod': undt})

@csrf_exempt
def underTerprod(request):
    subvisibleprod = request.POST['visible']
    upper = int(subvisibleprod)
    lower = upper - 12

    undterID = request.POST['id']
    undTer = UnderTertiaryCategory.objects.get(under_ter_category_id=undterID)
    getprod = Productmod.objects.filter(Q(prod_under_tertiary_category=undTer) & Q(is_approved=1)).values()[lower:upper]
    undt = list(getprod)
    return JsonResponse({'underTer': undt})


@csrf_exempt
def getprodbySize(request):
    subvisibleprod = request.POST['visible']
    upper = int(subvisibleprod)
    lower = upper - 12
    subID = request.POST['id']
    SizName = request.POST['siz']
    ClickSubCat = SubCategory.objects.get(sub_category_id=subID)
    print('ajax clicked subcat :-', ClickSubCat)
    prodsize = prodSize.objects.filter(size_name=SizName)
    prodlist = list()
    prulist = ''
    for su in prodsize:
        print(su.product)
        prulist = list(Productmod.objects.filter(Q(prod_custom_id=su.product.prod_custom_id)& Q(prod_sub_category=ClickSubCat) & Q(is_approved=1)).values()[lower:upper])
        prodlist.append(prulist)


    undt = prodlist

    return JsonResponse({'prod': undt})

@csrf_exempt
def relatedproduct(request):
    subvisibleprod = request.POST['visible']
    upper = int(subvisibleprod)
    lower = upper - 12
    subID = request.POST['id']
    SizName = request.POST['siz']
    ClickSubCat = SubCategory.objects.get(sub_category_id=subID)
    print('ajax clicked subcat :-', ClickSubCat)
    prodsize = prodSize.objects.filter(size_name=SizName)
    prodlist = list()
    prulist = ''
    for su in prodsize:
        print(su.product)
        prulist = list(Productmod.objects.filter(Q(prod_custom_id=su.product.prod_custom_id)& Q(prod_sub_category=ClickSubCat) & Q(is_approved=1)).values()[lower:upper])
        prodlist.append(prulist)


    undt = prodlist

    return JsonResponse({'prod': undt})




@csrf_exempt
def relatedProdSubCatpage(request):
    SubcatName = request.POST['undtername']
    getSubcatInstance = SubCategory.objects.get(sub_category_id=SubcatName)
    subvisibleprod = int(request.POST['visible'])
    upper = int(subvisibleprod)
    lower = upper - 3
    prod = Productmod.objects.filter(Q(prod_sub_category=getSubcatInstance) & Q(is_approved=1)).values()[lower:upper]


    podu = list(prod)

    return JsonResponse({
        'prod': podu,

    })



@csrf_exempt
def PODSubCatpage(request):

    subvisibleprod = int(request.POST['visible'])
    upper = int(subvisibleprod)
    lower = upper - 3
    prod = Productmod.objects.filter( Q(is_approved=1)).values()[lower:upper]

    podu = list(prod)

    return JsonResponse({
        'prod': podu,
    })
# =============================== Sub Category PAge end=====================================================





# =============================== single product page  =====================================================
@csrf_exempt
def relatedProdSingleProdpage(request):
    undterName = request.POST['undtername']
    getUndterInstance = UnderTertiaryCategory.objects.get(under_ter_category_id=undterName)
    subvisibleprod = int(request.POST['visible'])
    upper = int(subvisibleprod)
    lower = upper - 3
    prod = Productmod.objects.filter(Q(prod_under_tertiary_category=getUndterInstance) & Q(is_approved=1)).values()[lower:upper]


    podu = list(prod)

    return JsonResponse({
        'prod': podu,

    })



@csrf_exempt
def PODSingleProdpage(request):

    subvisibleprod = int(request.POST['visible'])
    upper = int(subvisibleprod)
    lower = upper - 3
    prod = Productmod.objects.filter( Q(is_approved=1)).values()[lower:upper]

    podu = list(prod)









# =============================== Indian hatt PAge =====================================================

@csrf_exempt
def Ihatttwntyprsnt(request):
    subvisibleprod = int(request.POST['visible'])
    upper = int(subvisibleprod)
    lower = upper - 8
    prod = Productmod.objects.filter( Q(is_approved=1)).values()[lower:upper]


    podu = list(prod)

    return JsonResponse({
        'prod': podu,

    })


# =============================== Indian hatt PAge end =====================================================


# ============= viewall Offers =======================
@csrf_exempt
def viewalloffersMore(request):
    offvisible = int(request.POST['visible'])
    upper = offvisible
    print(offvisible)
    lower = upper - 12
    offer = request.POST['id']
    print()
    print()
    print('offer id :- ', offer)
    offerName = offer
    off_instance = Offer.objects.get(offer_custom_id=offerName)
    products = Productmod.objects.filter(Q(Offer_Name=off_instance.offer_title) & Q(is_approved=1)).values()[lower:upper]

    print( )
    print()
    print()

    podu = list(products)

    return JsonResponse({
        'prod': podu,
    })


@csrf_exempt
def viewallofferscolFilter(request):
    col_id = request.POST['col']
    offvisible = int(request.POST['visible'])
    upper = offvisible
    print(offvisible)
    lower = upper - 12
    offer = request.POST['id']
    print()
    print()
    print('offer id :- ', offer)
    offerName = offer
    off_instance = Offer.objects.get(offer_custom_id=offerName)
    color_instance = Colour.objects.get(color_id=col_id)
    products = Productmod.objects.filter(Q(Offer_Name=off_instance.offer_title)& Q(prod_color=color_instance) & Q(is_approved=1)).values()[lower:upper]

    print()
    print()
    print()

    podu = list(products)

    return JsonResponse({
        'prod': podu,
    })
# ============= viewall Offers end =====================




# ============= viewall SubCat =======================
@csrf_exempt
def viewallSubcatMore(request):
    viewSubcat = int(request.POST['visible'])
    upper = viewSubcat
    lower = upper - 12
    SubcatID = request.POST['id']
    print()
    print()
    print('Subcat id :- ', SubcatID)

    Sucat_instance = SubCategory.objects.get(sub_category_id=SubcatID)
    products = Productmod.objects.filter(Q(prod_sub_category=Sucat_instance) & Q(is_approved=1) ).values()[lower:upper]

    print()
    print()
    print()

    podu = list(products)

    return JsonResponse({
        'prod': podu,
    })



@csrf_exempt
def viewallSubcatcolrFilter(request):
    col_id = request.POST['col']
    viewSubcat = int(request.POST['visible'])
    upper = viewSubcat
    lower = upper - 12
    SubcatID = request.POST['id']
    print()
    print()
    print('Subcat id :- ', SubcatID)

    Sucat_instance = SubCategory.objects.get(sub_category_id=SubcatID)
    color_instance = Colour.objects.get(color_id=col_id)
    products = Productmod.objects.filter(Q(prod_sub_category=Sucat_instance ) & Q(prod_color=color_instance) & Q(is_approved=1)).values()[lower:upper]

    print()
    print()
    print()

    podu = list(products)

    return JsonResponse({
        'prod': podu,
    })

# ============= viewall SubCat end =====================

@csrf_exempt
def CustomerView(request):
    prodid =  request.POST['id']
    print()
    print()
    print('prodid :- ', prodid)
    pro_instance = Productmod.objects.get(Q(prod_custom_id=prodid) & Q(is_approved=1))
    if pro_instance.Cutomer_Views == None:
        pro_instance.Cutomer_Views = 1
        pro_instance.save()
    else:
        pro_instance.Cutomer_Views += 1
        pro_instance.save()




    print(pro_instance.Cutomer_Views)
    print()
    print()


    return JsonResponse({
        'prod': 'Done',

    })

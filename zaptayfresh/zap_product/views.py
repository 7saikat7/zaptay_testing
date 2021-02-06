# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, TemplateView, FormView, ListView
from django.contrib import messages
import os
from django.db.models import Subquery, Q

from .zap_product_form import *
from .models import *
import uuid
from attribute.models import *
from seller.models import *
# from stock.models import Bach
# from user_login.models import UserAccount, UserWishList, UserCartList

from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Admin part
from admin_login.models import zaptayadmin
from seller_login.models import seller_login
# Create your views here.
import random


class ProductViewsDetails(TemplateView):
    template_name = 'product.html'
    '''
    def get(self, request, **kwargs):
        print (kwargs)
        return render(request, self.template_name)
    '''
    def get_context_data(self, **kwargs):
        context = dict()
        product_id = self.kwargs.get('product_slug')
        product_list = Product.objects.all().filter(prod_custom_id=product_id)
        product_image_list = ProductImage.objects.filter(
            product_id=product_list[0].id)
        product_show_image_list = list()
        if product_image_list:
            for p_image in product_image_list:
                product_image_dict = dict()
                product_image_dict['path'] = p_image.product_image
                product_image_dict['title'] = p_image.prod_image_title
                product_show_image_list.append(product_image_dict)
        product_stock_price = Bach.objects.filter(
            product_id=product_list[0].id)
        if product_stock_price:
            product_price_dic_percent = int(100 - (
                (float(product_stock_price[0].offer_price) /
                 float(product_stock_price[0].main_price)) * 100))
        else:
            product_price_dic_percent = ""

        # Relared Product fetch =========================
        related_product_list = list()
        relted_product_list_db = Product.objects.filter(
            Q(prod_tertiary_category__in=Product.objects.filter(
                prod_custom_id=product_id).values('prod_tertiary_category')),
            ~Q(prod_custom_id=product_id))
        if relted_product_list_db:
            for related_prod in relted_product_list_db:
                related_product_dict = dict()
                related_product_dict['product_name'] = related_prod.prod_title
                product_image_list = ProductImage.objects.filter(
                    product_id=related_prod.id, home_image=True).first()
                related_product_dict[
                    'product_image'] = product_image_list.product_image
                related_product_dict[
                    'product_image_title'] = product_image_list.prod_image_title

                related_product_stock_price = Bach.objects.filter(
                    product_id=related_prod.id)
                if related_product_stock_price:
                    related_product_dict['save_percent'] = int(100 - (
                        (float(related_product_stock_price[0].offer_price) /
                         float(related_product_stock_price[0].main_price)) *
                        100))
                    related_product_dict['save_amount'] = int(
                        float(related_product_stock_price[0].main_price) -
                        float(related_product_stock_price[0].offer_price))
                    related_product_dict[
                        'main_price'] = related_product_stock_price[
                            0].main_price
                    related_product_dict[
                        'offer_price'] = related_product_stock_price[
                            0].offer_price
                else:
                    related_product_dict['save_percent'] = ""
                    related_product_dict['save_amount'] = ""
                    related_product_dict['main_price'] = ""
                    related_product_dict['offer_price'] = ""

                related_product_list.append(related_product_dict)

        # Check user login
        user_detail = list()
        wish_list_count = ""
        get_wishlist_product = ""
        if self.request.COOKIES.get('user_id'):
            user_details_dict = dict()
            get_user_detail = UserAccount.objects.filter(
                user_custom_id=self.request.COOKIES.get('user_id'))
            user_details_dict[
                'name'] = get_user_detail[0].user_f_name.capitalize(
                ) + " " + get_user_detail[0].user_l_name.capitalize()
            user_detail.append(user_details_dict)

            # Get wish list items
            get_user_id = UserAccount.objects.filter(
                user_custom_id=self.request.COOKIES['user_id']).first()
            wish_list_count = UserWishList.objects.filter(
                user_id=get_user_id).count()
            get_wishlist_product = UserWishList.objects.filter(
                user_id=get_user_id)
            # print (get_wishlist_product)
            is_product_in_wishlist = UserWishList.objects.filter(
                user_id=get_user_id, product_id=product_list.first()).count()

            # Get Cart List Item
            cart_list_count = UserCartList.objects.filter(
                user_id=get_user_id).count()
            get_cart_product = UserCartList.objects.filter(user_id=get_user_id)
            is_product_in_cart = UserCartList.objects.filter(
                user_id=get_user_id, product_id=product_list.first()).count()

        context = {
            'product_all_desc': product_list.first(),
            'product_image': product_show_image_list,
            'product_stock_price': product_stock_price.first(),
            'price_discount': product_price_dic_percent,
            'relted_product': related_product_list,
            'login_user': user_detail,
            'total_wish_list': wish_list_count,
            'wish_list_product': get_wishlist_product,
            'this_product': is_product_in_wishlist,
            'total_cart_list': cart_list_count,
            'cart_product': get_cart_product,
            'cart_this_product': is_product_in_cart
        }
        return context


# *********************************************************************
# Ajax hendel in client side

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse


# @csrf_exempt
# def AddWishlist(request):

#     get_user_id = UserAccount.objects.filter(
#         user_custom_id=request.COOKIES['user_id']).first()
#     product_id = Product.objects.filter(
#         prod_custom_id=request.POST['product_id']).first()

#     add_wish_list = UserWishList(user_id=get_user_id, product_id=product_id)
#     add_wish_list.save()

#     data = {
#         'status': 'success',
#     }
#     return JsonResponse(data)





# ----------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------     Admin Part      ------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------
############################################ View All Product ########################################################
class ShowProductList(TemplateView):
    template_name = 'admin_templates/admin_all_product_templates/all_product.html'

    def dispatch(self, request, *args, **kwargs):
        try:
            resp = request.session['admin_email_id']
            return super(ShowProductList,
                         self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)
            # return redirect('/site-admin/login')
            return redirect('admin_login:admin_loginpage')

    def get_context_data(self, **kwargs):
        context = dict()
        get_name = zaptayadmin.objects.all().get(
            email_id=self.request.session['admin_email_id'])
        product_list = Productmod.objects.all().order_by('prod_custom_id')
        context = {
            "page_name": "product_list",
            "admin_name": get_name.admin_f_name + " " + get_name.admin_l_name,
            'product_list': product_list
        }
        return context


###################################### Show\add new Product Form #######################################################
class ShowProductForm(FormView):
    form_class = ProductForm
    template_name = 'admin_templates/admin_add_product_templates/product_form.html'
    success_url = '/zaptay-admin-login/product/product-form/'

    def dispatch(self, request, *args, **kwargs):
        try:
            resp = request.session['admin_email_id']
            return super(ShowProductForm,self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)
            return redirect('admin_login:admin_loginpage')




    def get_context_data(self, **kwargs):


        context = dict()
        imgfrm = ProductImageForm()
        get_name = zaptayadmin.objects.all().get(
            email_id=self.request.session['admin_email_id'])

        allsiz = Size.objects.values('size_name')
        print()
        print()
        print()
        print()
        print()
        print()
        print(allsiz)
        print()
        print()
        print()
        print()
        context = {
            'imgfrm': imgfrm,
            "page_name": "add_product",
            "admin_name": get_name.admin_f_name + " " + get_name.admin_l_name,
            'form': self.form_class,
            'Allsiz':allsiz
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
                print (product_image_array)
                sl_no = request.POST.getlist('product_sl_image')
                print (sl_no)
                # is_home_image_select = request.POST.getlist('product_home_image')
                # print (is_home_image_select)
                i = 0
                imagefirst = ''
                secondimg = ''
                thirdimg = ''
                fourthimg = ''
                fifthimg=''
                sixth = ''
                for product_image,sl_nunu in zip(product_image_array,sl_no):

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









                    i=i+1




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
                    is_approved=1)
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
                prod_instance =   Productmod.objects.all().get(prod_custom_id=Prod_id)
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
                    is_approved=1)
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


############################################# Edit Product ###############################################
class EditProduct(FormView):
    form_class = ProductForm
    template_name = 'admin_templates/admin_add_product_templates/product_form.html'
    success_url = '/zaptay-admin-login/product/product-form/'

    def dispatch(self, request, *args, **kwargs):
        try:
            resp = request.session['admin_email_id']
            return super(EditProduct, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)
            return redirect('admin_login:admin_loginpage')

    def get_context_data(self, **kwargs):
        prod_id = self.kwargs.get('Product_id')

        context = dict()
        prudukt = Productmod.objects.get(pk=prod_id)
        # imug = ProductImage.objects.get(prod_image_id=prudukt.prod_image_id)
        # print(imug)
        fm = ProductForm(
            initial={
                'product_title': prudukt.prod_title,
                'category': prudukt.prod_category,
                'sub_category': prudukt.prod_sub_category,
                'tertiary': prudukt.prod_tertiary_category,
                'under_tertiary': prudukt.prod_under_tertiary_category,
                'seller': prudukt.seller,
                'made_in': prudukt.prod_made_in,
                'brand': prudukt.prod_brand,
                'description': prudukt.prod_desc,
                'same_day_delivary_check': prudukt.same_day_delivery,
                'same_day_delivary_price': prudukt.same_day_delivery_price,
                'next_day_delivary_check': prudukt.next_day_delivery,
                'next_day_delivary_price': prudukt.next_day_delivery_price,
                'customize_delivary_check': prudukt.customize_day_delivery,
                'customize_delivary_day': prudukt.customize_day_delivery_day,
                'customize_delivary_price': prudukt.customize_day_delivery_price,
                'cod': prudukt.cash_on_delivery,
                'return_product': prudukt.product_return,
                'AddToOffer': prudukt.is_add2offer,
                'B2b_check': prudukt.is_b2b,
                'main_price': prudukt.m_price,
                'offer_price': prudukt.off_price,
                'color': prudukt.prod_color,
                'youtube': prudukt.youtube_link,
                'stock': prudukt.stock,
            })


        imgfrm = ProductImageForm()
        get_name = zaptayadmin.objects.all().get(email_id=self.request.session['admin_email_id'])
        allsiz = Size.objects.values('size_name')
        context = {
            'imgfrm': imgfrm,
            "page_name": "add_product",
            "admin_name": get_name.admin_f_name + " " + get_name.admin_l_name,
            'form': fm,
            'proid': prod_id,
            'Allsiz': allsiz
        }
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        Uprod_id = self.kwargs.get('Product_id')
        print(Uprod_id)

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
                product_title = product_titlee
                for product_image in product_image_array:
                    fs = FileSystemStorage()
                    image_title = product_title + "." + product_image.name.split(
                        '.')[-1]
                    image_title = image_title.replace(" ", "")
                    upload_image = fs.save("products/images/" + image_title,
                                           product_image)
                    img_url = fs.url(upload_image)
                    mod_image_name = img_url.split("/")[-1]
                    image_path = 'products/images/' + mod_image_name
                    print('image path :-' + image_path)
                    print('image title :-' + image_title)
                    print('image url :-' + img_url)



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
                Uproduct = Productmod.objects.get(prod_custom_id=Uprod_id)
                Uproduct.prod_title = product_titlee
                Uproduct.prod_category = caT_instance
                Uproduct.prod_sub_category = Sub_caT_instance
                Uproduct.prod_tertiary_category = Ter_instance
                Uproduct.prod_under_tertiary_category = UnderT_instance
                Uproduct.prod_brand = Brand_instance
                Uproduct.prod_made_in = Made_in_instance
                Uproduct.prod_desc = describtion
                Uproduct.seller = Selr_instance
                Uproduct.same_day_delivery = sameDayDel
                Uproduct.same_day_delivery_price = sameDayDelPrice
                Uproduct.next_day_delivery = nxtDayDel
                Uproduct.next_day_delivery_price = nxtDayDelPrice
                Uproduct.customize_day_delivery = custDel
                Uproduct.customize_day_delivery_day = custDelDay
                Uproduct.customize_day_delivery_price = custDelPrice
                Uproduct.product_return = Return
                Uproduct.cash_on_delivery = cod
                Uproduct.m_price = mPrice
                Uproduct.is_add2offer = addToOffer
                Uproduct.off_price = offerPrice
                Uproduct.is_b2b = b2b_check
                Uproduct.stock = Stock
                if Utube != '':
                    Uproduct.youtube_link = Utube
                Uproduct.prod_color = color_instance


                Uproduct.save()

        except Exception as e:
            print('post exception main form')
            print(e)

        #Getting More Add Form Data
        try:
            if 'prod_idimg' in request.POST:
                Prod_id = request.POST['prod_idimg']
                if Prod_id != '':
                    Proddd_instance = Productmod.objects.all().get(
                        prod_custom_id=Prod_id)

            if 'colorimg' in request.POST:
                Color = request.POST['colorimg']
                color_instance = Colour.objects.all().get(color_id=Color)
                print(color_instance)

            if 'stockimg' in request.POST:
                Stock = request.POST['stockimg']
                print(Stock)

            if 'youtubeimg' in request.POST:
                Utubeee = request.POST['youtubeimg']
                print(Utubeee)

            if 'main_priceimg' in request.POST:
                M_price = request.POST['main_priceimg']
                print(M_price)

            if 'sell_priceimg' in request.POST:
                S_price = request.POST['sell_priceimg']
                print(S_price)

            if 'product_imageimg' in request.FILES:
                product_image_array = request.FILES.getlist('product_imageimg')
                print(product_image_array)
                product_title = "yo bro"
                for product_image in product_image_array:
                    fs = FileSystemStorage()
                    image_title = product_title + "." + product_image.name.split(
                        '.')[-1]
                    image_title = image_title.replace(" ", "")
                    upload_image = fs.save("products/images/" + image_title,
                                           product_image)
                    img_url = fs.url(upload_image)
                    mod_image_name = img_url.split("/")[-1]
                    image_path = 'products/images/' + mod_image_name
                    print('image path :-' + image_path)
                    print('image title :-' + image_title)
                    print('image url :-' + img_url)

            if 'sizeSimg' in request.POST:
                sizes = True
                print(sizes)

            if 'sizeMimg' in request.POST:
                sizem = True
                print(sizem)

            if 'sizeLimg' in request.POST:
                sizel = True
                print(sizel)

            if 'sizeXLimg' in request.POST:
                sizexl = True
                print(sizexl)

            if 'sizeXXLimg' in request.POST:
                sizexxl = True
                print(sizexxl)

            #Uproduct = Productmod.objects.get(prod_custom_id=Uprod_id)
            #print(Uproduct)
            #prodImdUpdate = ProductImage.objects.get(prod_image_id=Uproduct.prod_image_id)
            #print(prodImdUpdate)
            #prodImdUpdate.prod_custom_id = Proddd_instance
            #prodImdUpdate.youtube_link = Utubeee
            #prodImdUpdate.prod_color = color_instance
            #prodImdUpdate.m_price = M_price
            #prodImdUpdate.off_price=S_price

            #prodImdUpdate.save()

        except Exception as e:
            print('post exception')
            print(e)

        context = self.get_context_data()
        context['form'] = form

        return self.render_to_response(context)


######################################### B2B ##########################################################
class B2Bview(TemplateView):
    template_name = 'admin_templates/admin_B2B_templates/admin_B2B_show_all_data.html'

    def dispatch(self, request, *args, **kwargs):
        try:
            resp = request.session['admin_email_id']
            return super(B2Bview, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)
            # return redirect('/site-admin/login')
            return redirect('admin_login:admin_loginpage')

    def get_context_data(self, **kwargs):
        context = dict()
        get_name = zaptayadmin.objects.all().get(
            email_id=self.request.session['admin_email_id'])
        product_list = Productmod.objects.all().filter(is_b2b=True)
        print(product_list)
        context = {
            "page_name": "product_list",
            "admin_name": get_name.admin_f_name + " " + get_name.admin_l_name,
            'b2b_product_list': product_list
        }
        return context


#####################################################################################
#####################################################################################
#####################################################################################





# ******************************************************************************************************************

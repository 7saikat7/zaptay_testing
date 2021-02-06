from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, TemplateView, FormView
from django.contrib import messages
from django.db.models import Subquery, Q

from attribute.models import *
# from banner.models import Banner

from zap_product.models import *
# from stock.models import Bach
# from user_login.models import UserAccount

# Admin part
from admin_login.models import zaptayadmin
# from . add_main_category_form import AddMainCategoryForm
from . attribute_forms import *
# from home.base_template import BaseTemplateHeader

# Create your views here.

class CategoryViews(TemplateView):
    # template_name = 'category.html'
    template_name = 'user_templates/attributes_user_part/subcategory.html'

    def get_context_data(self, **kwargs):
        context = dict()

        get_sub_category = self.kwargs.get('category')
        get_tertiory_category = self.kwargs.get('tertiarycategory')

        # banner ================================================================================
        #left_banner = Banner.objects.filter(banner_name='advatice_left').first()
        #right_banner = Banner.objects.filter(banner_name='advatice_right').first()
        #middle_banner = Banner.objects.filter(banner_name=get_sub_category+"_banner")

        # Search the subcategory from seo url ===================================
        get_sub_category_id = SubCategory.objects.filter(sub_category_seo_url=get_sub_category).first()

        # Search tertiory category from sub_category =========================================
        # Variable assign =====================================
        tertiory_categories = list()
        get_under_tertiory_category = list()

        # If teritory_category None Start **************************************************
        if get_tertiory_category == None:
            breadcrumbs_category = {'sub_category': get_sub_category_id.sub_category_name}
            get_tertiory_categories = TertiaryCategory.objects.filter(sub_category_id=get_sub_category_id)
            if get_tertiory_categories:
                for index, data in enumerate(get_tertiory_categories):
                    # print (index, data)
                    focus = 0

                    if index == 0:
                        focus = 1
                    tertiory_categories.append({'tertiory_name': data.ter_category_name, 'image': data.tertiary_category_image, 'focus': focus})

                get_under_tertiory_category = UnderTertiaryCategory.objects.filter(ter_category_id=get_tertiory_categories[0])


        obj = BaseTemplateHeader(self.request)
        base_template_data = obj.GetHeaderContent()

        context = {
            'base_template_content': base_template_data,

            #'sides_banners': {'left': left_banner, 'right': right_banner, 'middle_banner': middle_banner},
            'breadcrumbs_category': breadcrumbs_category,
            'tertiory_category': tertiory_categories,
            'under_tertiory_category': get_under_tertiory_category,
        }
        return context



class ProductViews(TemplateView):
    template_name = 'product.html'



    def get(self, request, **kwargs):

        print (kwargs)
        return render(request, self.template_name)

# Get Ajax data
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse

@csrf_exempt
def ProductFetch(request):
    tertiary_id = request.GET.get('tertiary_id')
    tertiary_name = request.GET.get('tertiary_name')

    # Fetch product by tertiary category
    product_list = list()
    product_list_db = Product.objects.filter(prod_tertiary_category=tertiary_id)
    for product in product_list_db:
        product_dict = dict()
        product_dict['id'] = product.prod_custom_id
        product_dict['name'] = product.prod_title
        product_image_db = ProductImage.objects.filter(product_id=product, home_image=True)
        if product_image_db:
            product_dict['image_path'] = str(product_image_db[0].product_image)
            product_dict['image_title'] = str(product_image_db[0].prod_image_title)
        else:
            product_dict['image_path'] = ''
            product_dict['image_title'] = product.prod_title
        # print (product_image_db)
        product_price_list_db = MadeIn.objects.filter(product_id=product)
        if product_price_list_db:
            product_dict['product_main_price'] = product_price_list_db[0].main_price
            product_dict['product_offer_price'] = product_price_list_db[0].offer_price
            product_dict['product_price_save'] = int(float(product_price_list_db[0].main_price)-float(product_price_list_db[0].offer_price))
            product_dict['product_price_off_percent'] = int(100-((float(product_price_list_db[0].offer_price)/float(product_price_list_db[0].main_price))*100))
        else:
            product_dict['product_main_price'] = ''
            product_dict['product_offer_price'] = ''
            product_dict['product_price_save'] = ''
            product_dict['product_price_off_percent'] = ''

        product_list.append(product_dict)
    # print (product_list)

    data = {
        'status': 'success',
        'resp': product_list
    }
    return JsonResponse(data)

#  ----+++++++++++++++++++++++++++++************** Admin part **********+++++++++++++++++++++++++++++++++++-------------------------------------------------------------------------------------------------------------------

class AddMainCategory(FormView):
    template_name = 'admin_templates/admin_attribute_templates/main_category_form.html'
    form_class = AddMainCategoryForm
    success_url = '/site-admin/category/add-main-category/'

    def dispatch(self, request, *args, **kwargs):
        try:
            resp = request.session['admin_email_id']
            return super(AddMainCategory, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)
            # return redirect('/site-admin/login')
            return redirect('admin_login:admin_loginpage')

    def get_context_data(self, **kwargs):
        context = dict()
        get_name = zaptayadmin.objects.all().get(email_id=self.request.session['admin_email_id'])
        context = {"page_name": "main_category", "admin_name": get_name.admin_f_name+" "+get_name.admin_f_name, "form": self.form_class}
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            try:
                category_name = request.POST['category_name']
                context = self.get_context_data(task_form=form)
                context['success'] = "success"
                # return self.form_valid(form) #THIS IS 100% OK

                # Insert into database
                admin_id = zaptayadmin.objects.all().get(email_id=request.session.get('admin_email_id'))
                add_main_category = MainCategory(main_category_name=category_name, added_by=admin_id)
                add_main_category.save()
                return self.render_to_response(context)
            except Exception as e:
                print (e)
                return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        context = self.get_context_data(task_form=form)
        context['error'] = form
        return self.render_to_response(context)

# ========================================================================================================================
class ShowAllMainCategory(TemplateView):
    template_name = 'admin_templates/admin_attribute_templates/show_all_main_category.html'

    def dispatch(self, request, *args, **kwargs):
        try:
            resp = request.session['admin_email_id']
            return super(ShowAllMainCategory, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)
            return redirect('admin_login:admin_loginpage')

    def get_context_data(self, **kwargs):
        # Fetch data
        main_cartegory_data = MainCategory.objects.all().order_by('-category_id')
        context = dict()
        get_name = zaptayadmin.objects.all().get(email_id=self.request.session['admin_email_id'])
        context = {"page_name": "main_category", "admin_name": get_name.admin_f_name+" "+get_name.admin_f_name, "main_category": main_cartegory_data}
        return context




class AddSubCategory(FormView):
    template_name = 'admin_templates/admin_attribute_templates/sub_category_form.html'
    form_class = AddSubCategoryForm
    success_url = '/site-admin/category/add-sub-category/'

    def dispatch(self, request, *args, **kwargs):
        try:
            resp = request.session['admin_email_id']
            return super(AddSubCategory, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)
            # return redirect('/site-admin/login')
            return redirect('admin_login:admin_loginpage')

    def get_context_data(self, **kwargs):
        context = dict()
        get_name = zaptayadmin.objects.all().get(email_id=self.request.session['admin_email_id'])
        context = {"page_name": "main_category", "admin_name": get_name.admin_f_name+" "+get_name.admin_f_name, "form": self.form_class}
        return context

    def form_invalid(self, form):
        context = self.get_context_data(task_form=form)
        context['error'] = form
        return self.render_to_response(context)

# ============================================== Mainly Used =========================================================================


class AttributeList(FormView):
    template_name = 'admin_templates/admin_attribute_templates/attributes.html'
    # form_class = CategoryForm
    category_form_class = CategoryForm
    sub_category_form_class = SubcategoryForm
    teri_category_class = TertiaryCategoryForm
    under_teri_category_class = UnderTertiaryCategoryForm
    brand_class = BrandForm
    color_class = ColorForm
    size_class = SizeForm
    source_class = MadeInForm
    same_day_pincode_class = SameDayPincodeForm
    next_day_pincode_class = NextDayPincodeForm

    def dispatch(self, request, *args, **kwargs):
        try:
            resp = request.session['admin_email_id']
            return super(AttributeList, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)
            # return redirect('/site-admin/login')
            return redirect('admin_login:admin_loginpage')

    def get_context_data(self, **kwargs):
        context = dict()
        get_name = zaptayadmin.objects.all().get(email_id=self.request.session['admin_email_id'])
        category_list = MainCategory.objects.all()
        sub_category_list = SubCategory.objects.all()
        ter_caregory_list = TertiaryCategory.objects.all()
        under_ter_caregory_list = UnderTertiaryCategory.objects.all()
        brand_list = Brand.objects.all()
        color_list = Colour.objects.all()
        size_list = Size.objects.all()
        source_list = MadeIn.objects.all()
        same_day_delivary_pin_list = SameDayDelivary.objects.all()
        next_day_delivary_pin_list = NextDayDelivary.objects.all()

        # print (sub_category_list[0].category_id.main_category_name) # Worked
        # Teritory category with sub category and category
        ter_caregory_list_2 = list()
        for category in category_list:
            print (category.main_category_name)
            get_sub_category = SubCategory.objects.filter(category_id=category)
            for sub_category in get_sub_category:
                print ("\t"+sub_category.sub_category_name)
                get_tertiary_category = TertiaryCategory.objects.filter(sub_category_id=sub_category)
                for tertiary_category in get_tertiary_category:
                    print ("\t\t"+tertiary_category.ter_category_name)


        context = {
            "page_name": "attribute",
            "admin_name": get_name.admin_f_name+" "+get_name.admin_f_name,
            "category_list": category_list,
            "sub_category_list": sub_category_list,
            "ter_category_list": ter_caregory_list,
            "under_ter_caregory_list": under_ter_caregory_list,
            "brand_list": brand_list,
            "color_list": color_list,
            "size_list": size_list,
            "source_list": source_list,
            "same_day_pin_list": same_day_delivary_pin_list,
            "next_day_pin_list": next_day_delivary_pin_list}

        context['category_form'] = self.category_form_class
        context['sub_category_form'] = self.sub_category_form_class
        context['tertia_form'] = self.teri_category_class
        context['under_tertia_form'] = self.under_teri_category_class
        context['brand_form'] = self.brand_class
        context['color_form'] = self.color_class
        context['size_form'] = self.size_class
        context['source_form'] = self.source_class
        context['same_day_pincode_form'] = self.same_day_pincode_class
        context['next_day_pincode_form'] = self.next_day_pincode_class
        return context

    def post(self, request, *args, **kwargs):


        if 'category_add_form' in request.POST:
            category_form = CategoryForm(request.POST)

            if category_form.is_valid():
                category_name = request.POST['category_add_form'].lower()
                admin_id = zaptayadmin.objects.all().get(email_id=request.session.get('admin_email_id'))
                insert_que = MainCategory(main_category_name = category_name, added_by = admin_id)
                insert_que.save()
                messages.success(request, "Catagory added", extra_tags='category')
            else:
                messages.error(request, "All fields mentetory", extra_tags='category')



        if 'sub_category_add_form' in request.POST:
            sub_category_from = SubcategoryForm(request.POST)

            if sub_category_from.is_valid():
                main_category_id = request.POST['category_list']
                sub_category_name = request.POST['sub_category_add_form']

                admin_id = zaptayadmin.objects.all().get(email_id=request.session.get('admin_email_id'))
                get_category_id = MainCategory.objects.get(pk=main_category_id)
                insert_que = SubCategory(sub_category_name=sub_category_name, added_by=admin_id, category_id=get_category_id)
                insert_que.save()
                messages.success(request, "Sub catagory added", extra_tags='sub_category')
                # print (main_category_id, sub_category_name, get_category_id)
            else:
                # select_category = request.POST['']
                messages.error(request, "All fields mentetory", extra_tags='sub_category')




        if 'tert_category_add_form' in request.POST:
            sub_category_from = TertiaryCategoryForm(request.POST)

            if sub_category_from.is_valid():
                sub_category_id = request.POST['sub_category_list']
                tert_category_name = request.POST['tert_category_add_form']

                admin_id = zaptayadmin.objects.all().get(email_id=request.session.get('admin_email_id'))
                get_sub_category = SubCategory.objects.get(pk=sub_category_id)

                insert_que = TertiaryCategory(ter_category_name=tert_category_name, added_by=admin_id, sub_category_id=get_sub_category)
                insert_que.save()
                messages.success(request, "Tertiary catagory added", extra_tags='terriary_category')
            else:
                messages.error(request, "All fields mentetory", extra_tags='terriary_category')





        if 'under_tert_category_add_form' in request.POST:
            under_tertiary_category_from = UnderTertiaryCategoryForm(request.POST)

            if under_tertiary_category_from.is_valid():
                tert_category_id = request.POST['tert_category_list']
                under_tert_category_name = request.POST['under_tert_category_add_form']

                # print (tert_category_id, under_tert_category_name, '************************')

                admin_id = zaptayadmin.objects.all().get(email_id=request.session.get('admin_email_id'))
                get_tert_category = TertiaryCategory.objects.get(pk=tert_category_id)

                # print (get_tert_category, "******************************************")

                insert_que = UnderTertiaryCategory(under_ter_category_name=under_tert_category_name, added_by=admin_id, ter_category_id=get_tert_category)
                insert_que.save()
                messages.success(request, "Under tertiary catagory added", extra_tags='under_terriary_category')
            else:
                messages.error(request, "All fields mentetory", extra_tags='under_terriary_category')




        if 'brand_add_form' in request.POST:
            brand_from = BrandForm(request.POST)

            if brand_from.is_valid():
                brand_name = request.POST['brand_add_form'].lower()
                # print (brand_name, "*******************")

                admin_id = zaptayadmin.objects.all().get(email_id=request.session.get('admin_email_id'))

                insert_que = Brand(brand_name=brand_name, added_by=admin_id)
                insert_que.save()
                messages.success(request, "Brand added", extra_tags='brand')
            else:
                messages.error(request, "All fields mentetory", extra_tags='brand')

        if 'color_add_form' in request.POST:
            color_from = ColorForm(request.POST)

            if color_from.is_valid():
                color_name = request.POST['color_add_form'].lower()

                admin_id = zaptayadmin.objects.all().get(email_id=request.session.get('admin_email_id'))

                insert_que = Colour(color_name=color_name, added_by=admin_id)
                insert_que.save()
                messages.success(request, "Color added", extra_tags='colour')
            else:
                messages.error(request, "All fields mentetory", extra_tags='colour')

        if 'size_add_form' in request.POST:
            size_from = SizeForm(request.POST)

            if size_from.is_valid():
                size = request.POST['size_add_form'].lower()

                admin_id = zaptayadmin.objects.all().get(email_id=request.session.get('admin_email_id'))

                insert_que = Size(size_name=size, added_by=admin_id)
                insert_que.save()
                messages.success(request, "Size added", extra_tags='size')
            else:
                messages.error(request, "All fields mentetory", extra_tags='size')

        if 'source_add_form' in request.POST:
            size_from = MadeInForm(request.POST)

            if size_from.is_valid():
                source = request.POST['source_add_form'].lower()

                admin_id = zaptayadmin.objects.all().get(email_id=request.session.get('admin_email_id'))

                insert_que = MadeIn(source_name=source, added_by=admin_id)
                insert_que.save()
                messages.success(request, "Source added", extra_tags='source')
            else:
                messages.error(request, "All fields mentetory", extra_tags='source')

        if 'same_day_pin_add_form' in request.POST:
            same_day_pin_form = SameDayPincodeForm(request.POST)

            if same_day_pin_form.is_valid():
                pin_code_no = request.POST['same_day_pin_add_form']

                admin_id = zaptayadmin.objects.all().get(email_id=request.session.get('admin_email_id'))

                insert_que = SameDayDelivary(pincode=pin_code_no, added_by=admin_id)
                insert_que.save()
                messages.success(request, "pincode added", extra_tags='same_day_pin')
            else:
                messages.error(request, "All fields mentetory", extra_tags='same_day_pin')

        if 'next_day_pin_add_form' in request.POST:
            next_day_pin_form = NextDayPincodeForm(request.POST)

            if next_day_pin_form.is_valid():
                pin_code_no = request.POST['next_day_pin_add_form']

                admin_id = zaptayadmin.objects.all().get(email_id=request.session.get('admin_email_id'))

                insert_que = NextDayDelivary(pincode=pin_code_no, added_by=admin_id)
                insert_que.save()
                messages.success(request, "pincode added", extra_tags='next_day_pin')
            else:
                messages.error(request, "All fields mentetory", extra_tags='next_day_pin')

        return render(request, self.template_name, self.get_context_data())

    def form_invalid(self, form):
        context = self.get_context_data(task_form=form)
        context['error'] = form
        print (context)
        return self.render_to_response(context)








def setcolImage(request):

    coloirid = request.POST['colorid']
    colorimg = request.FILES['setcolorimg']
    color = Colour.objects.get(color_id=coloirid)
    color.ColorImage = colorimg
    color.save()
    return HttpResponseRedirect('/zaptay-admin-login/attribute/')


def setbrandImage(request):

    brandid = request.POST['brandid']
    brandimg = request.FILES['setbrandimg']
    print()
    print()
    print('brandid id :- ', brandid)
    print('brandimg img :- ', brandimg)
    print()
    print()
    brand = Brand.objects.get(brand_id=brandid)
    brand.BrandImage = brandimg
    brand.save()


    return HttpResponseRedirect('/zaptay-admin-login/attribute/')


# Modify data runtime

from django.http import JsonResponse
def SendCategoryData(request):

    category_dict = dict()
    category_arr = list()

    category_list = MainCategory.objects.all()
    for i in category_list:
        category_arr.append([i.category_id , i.main_category_name])
        # print (i.category_id, i.main_category_name)
    category_dict['data'] = category_arr
    # print (category_dict)

    responseData = {
        'id': 4,
        'name': 'Test Response',
        'roles' : ['Admin','User']
    }
    return JsonResponse(category_dict)

def SendSubCategoryData(request):

    category_dict = dict()
    category_arr = list()

    category_list = SubCategory.objects.all()
    for i in category_list:
        category_arr.append([i.sub_category_id , i.sub_category_name])
    category_dict['data'] = category_arr

    return JsonResponse(category_dict)

def SendTertiaryCategoryData(request):

    category_dict = dict()
    category_arr = list()

    category_list = TertiaryCategory.objects.all()
    for i in category_list:
        category_arr.append([i.ter_category_id , i.ter_category_name])
    category_dict['data'] = category_arr

    return JsonResponse(category_dict)

def DeleteAttrinutsData(request):
    attribute_id = request.POST['attribute_id']
    attribut_attribute_type = request.POST['attribute_type']

    # print (attribute_id, attribut_attribute_type)

    if attribut_attribute_type == 'category':
        get_data = MainCategory.objects.get(pk=attribute_id)
        get_data.delete()

    if attribut_attribute_type == 'sub_category':
        get_data = SubCategory.objects.get(pk=attribute_id)
        get_data.delete()

    if attribut_attribute_type == 'tertiary_category':
        get_data = TertiaryCategory.objects.get(pk=attribute_id)
        get_data.delete()

    if attribut_attribute_type == 'under_tertiary_category':
        get_data = UnderTertiaryCategory.objects.get(pk=attribute_id)
        get_data.delete()

    if attribut_attribute_type == 'brand':
        get_data = Brand.objects.get(pk=attribute_id)
        get_data.delete()

    if attribut_attribute_type == 'color':
        get_data = Colour.objects.get(pk=attribute_id)
        get_data.delete()

    if attribut_attribute_type == 'size':
        get_data = Size.objects.get(pk=attribute_id)
        get_data.delete()

    if attribut_attribute_type == 'source':
        get_data = MadeIn.objects.get(pk=attribute_id)
        get_data.delete()

    if attribut_attribute_type == 'same_day_pin':
        get_data = SameDayDelivary.objects.get(pk=attribute_id)
        get_data.delete()

    if attribut_attribute_type == 'next_day_pin':
        get_data = NextDayDelivary.objects.get(pk=attribute_id)
        get_data.delete()

    resp = {
        "response": 'success'
    }

    return JsonResponse(resp)


def SendSortSubCategory(request):
    try:
        category_id = request.GET['category_id']

        category_dict = dict()
        category_arr = list()

        category_list = SubCategory.objects.all().filter(category_id=category_id)
        for i in category_list:
            category_arr.append([i.sub_category_id , i.sub_category_name])
        category_dict['data'] = category_arr

        return JsonResponse(category_dict)

    except Exception as e:
        print ("*********************************************************************************************************************************")
        print ("Error in ajax", e)
        print ("*********************************************************************************************************************************")

        resp = {
            "response": 'Failed'
        }

        return JsonResponse(resp)

def TertiarySubCategory(request):
    try:
        sub_category_id = request.GET['sub_category_id']

        category_dict = dict()
        category_arr = list()

        category_list = TertiaryCategory.objects.all().filter(sub_category_id=sub_category_id)
        for i in category_list:
            category_arr.append([i.ter_category_id , i.ter_category_name])
        category_dict['data'] = category_arr

        return JsonResponse(category_dict)

    except Exception as e:
        print ("*********************************************************************************************************************************")
        print ("Error in ajax", e)
        print ("*********************************************************************************************************************************")

        resp = {
            "response": 'Failed'
        }

        return JsonResponse(resp)

def SendUnderTertiaryCategory(request):
    try:
        tertiary_category_id = request.GET['tert_category_id']

        category_dict = dict()
        category_arr = list()

        category_list = UnderTertiaryCategory.objects.all().filter(ter_category_id=tertiary_category_id)
        for i in category_list:
            category_arr.append([i.under_ter_category_id , i.under_ter_category_name])
        category_dict['data'] = category_arr

        return JsonResponse(category_dict)

    except Exception as e:
        print ("*********************************************************************************************************************************")
        print ("Error in ajax", e)
        print ("*********************************************************************************************************************************")

        resp = {
            "response": 'Failed'
        }

        return JsonResponse(resp)

def GetAllBrands(request):
    try:
        category_dict = dict()
        category_arr = list()

        category_list = Brand.objects.all()
        for i in category_list:
            category_arr.append([i.brand_id , i.brand_name])
        category_dict['data'] = category_arr

        return JsonResponse(category_dict)

    except Exception as e:
        print ("*********************************************************************************************************************************")
        print ("Error in ajax", e)
        print ("*********************************************************************************************************************************")

        resp = {
            "response": 'Failed'
        }

        return JsonResponse(resp)

def GetAllColors(request):
    try:
        category_dict = dict()
        category_arr = list()

        category_list = Colour.objects.all()
        for i in category_list:
            category_arr.append([i.color_id , i.color_name])
        category_dict['data'] = category_arr

        return JsonResponse(category_dict)

    except Exception as e:
        print ("*********************************************************************************************************************************")
        print ("Error in ajax", e)
        print ("*********************************************************************************************************************************")

        resp = {
            "response": 'Failed'
        }

        return JsonResponse(resp)

def GetAllSize(request):
    try:
        category_dict = dict()
        category_arr = list()

        category_list = Size.objects.all()
        for i in category_list:
            category_arr.append([i.size_id , i.size_name])
        category_dict['data'] = category_arr

        return JsonResponse(category_dict)

    except Exception as e:
        print ("*********************************************************************************************************************************")
        print ("Error in ajax", e)
        print ("*********************************************************************************************************************************")

        resp = {
            "response": 'Failed'
        }

        return JsonResponse(resp)

def GetAllMadeIn(request):
    try:
        category_dict = dict()
        category_arr = list()

        category_list = MadeIn.objects.all()
        for i in category_list:
            category_arr.append([i.source_id , i.source_name])
        category_dict['data'] = category_arr

        return JsonResponse(category_dict)

    except Exception as e:
        print ("*********************************************************************************************************************************")
        print ("Error in ajax", e)
        print ("*********************************************************************************************************************************")

        resp = {
            "response": 'Failed'
        }

        return JsonResponse(resp)

def GetSubCategoryDetails(request):
    category_type = request.GET['category_type']
    sub_category = request.GET['sub_category_id']

    category_dict = dict()
    category_arr = list()

    # category_list = MainCategory.objects.filter(category_id__in=Subquery(SubCategory.objects.all().filter(sub_category_id=sub_category_id).values('category_id')))
    # print (category_list[0].main_category_name)

    if category_type != "tertiary_category":
        category_list = SubCategory.objects.all().filter(sub_category_id=sub_category).values('sub_category_id', 'sub_category_name', 'sub_category_image')
        for i in category_list:
            # category_arr.append([i.sub_category_id , i.sub_category_name])
            category_dict['sub_category_id'] = i['sub_category_id'];
            category_dict['sub_category_name'] = i['sub_category_name'].replace("_", " ");
            category_dict['sub_category_image'] = i['sub_category_image'];
        category_dict['data'] = category_arr
    else:
        category_list = TertiaryCategory.objects.all().filter(ter_category_id=sub_category).values('ter_category_id', 'ter_category_name', 'tertiary_category_image')
        for i in category_list:
            # category_arr.append([i.sub_category_id , i.sub_category_name])
            category_dict['sub_category_id'] = i['ter_category_id'];
            category_dict['sub_category_name'] = i['ter_category_name'].replace("_", " ");
            category_dict['sub_category_image'] = i['tertiary_category_image'];
        category_dict['data'] = category_arr

    resp = {
        "response": 'Failed'
    }
    return JsonResponse(category_dict)


# AJAX Image Upload
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def AjaxImageUpload(request):
    if 'sub_category_image' in request.FILES:
        sub_category_id = request.POST['sub_category_id']
        sub_category_name = request.POST['sub_category_name']
        sub_category_image = request.FILES['sub_category_image']
        sub_category_type = request.POST['sub_category_type']
        # print (sub_category_id,sub_category_name,sub_category_image.name)


        if sub_category_type == "tertiary_category":
            fs = FileSystemStorage()
            image_title = sub_category_name+"."+sub_category_image.name.split('.')[-1]
            image_title = image_title.replace(" ", "")
            upload_image = fs.save("Analyse/images/"+image_title, sub_category_image)
            img_url = fs.url(upload_image)
            mod_image_name = img_url.split("/")[-1]
            image_path = 'Analyse/images/'+mod_image_name
            # print (image_path)

            sub_category_details = TertiaryCategory.objects.filter(ter_category_id=sub_category_id)
            if sub_category_details[0].tertiary_category_image != "":
                os.remove('media/'+str(sub_category_details[0].tertiary_category_image))
                sub_category_details.update(tertiary_category_image = image_path)
            else:
                sub_category_details.update(tertiary_category_image=image_path)





        if sub_category_type == "sub_category":
            fs = FileSystemStorage()
            image_title = sub_category_name+"."+sub_category_image.name.split('.')[-1]
            image_title = image_title.replace(" ", "")
            upload_image = fs.save("sub_category/images/"+image_title, sub_category_image)
            img_url = fs.url(upload_image)
            mod_image_name = img_url.split("/")[-1]
            image_path = 'sub_category/images/'+mod_image_name
            # print (image_path)

            sub_category_details = SubCategory.objects.filter(sub_category_id=sub_category_id)
            if sub_category_details[0].sub_category_image != "":
                os.remove('media/'+str(sub_category_details[0].sub_category_image))
                sub_category_details.update(sub_category_image = image_path)
            else:
                sub_category_details.update(sub_category_image = image_path)



        if sub_category_type == "under_tertiary_category":
            fs = FileSystemStorage()
            image_title = sub_category_name+"."+sub_category_image.name.split('.')[-1]
            image_title = image_title.replace(" ", "")
            upload_image = fs.save("under_tertiary_category/images/"+image_title, sub_category_image)
            img_url = fs.url(upload_image)
            mod_image_name = img_url.split("/")[-1]
            image_path = 'sub_category/images/'+mod_image_name
            # print (image_path)

            sub_category_details = UnderTertiaryCategory.objects.filter(sub_category_id=sub_category_id)
            if sub_category_details[0].sub_category_image != "":
                os.remove('media/'+str(sub_category_details[0].sub_category_image))
                sub_category_details.update(sub_category_image = image_path)
            else:
                sub_category_details.update(sub_category_image = image_path)




        resp = {
            "response": 'success'
        }
        return JsonResponse(resp)

    resp = {
        "response": 'Failed'
    }
    return JsonResponse(resp)

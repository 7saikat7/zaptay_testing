from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from admin_login.models import zaptayadmin
from .models import *

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from banner.forms import *
# Create your views here.

class ViewBanner(TemplateView):
    template_name = 'admin_templates/admin_banner_templates/all_banner_list.html'

    def dispatch(self, request, *args, **kwargs):
        try:
            resp = request.session['admin_email_id']
            return super(ViewBanner, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)
            # return redirect('/site-admin/seller/seller-view/')
            return redirect('admin_login:admin_loginpage')

    def post(self, request, *args, **kwargs):
        try:
            # banner_name = request.POST['Banner_category']
            # print('banner name 1')
            # print(banner_name)















            if 'bannerimg' in request.FILES:
                banner_name = request.POST['Banner_category']
                banName = SubCategory.objects.get(sub_category_id=banner_name)
                print('banner name')
                print(banName.sub_category_name)
                banner_link = request.POST.getlist('banner_link')
                men_banner_image = request.FILES.getlist('bannerimg')
                for image, link in zip(men_banner_image, banner_link):
                    print (image)
                    print (link)
                    fs = FileSystemStorage()
                    image_title = "men-fashion-banner."+image.name.split(".")[-1]
                    upload_image = fs.save("banner/images/"+image_title, image)
                    img_url = fs.url(upload_image)
                    mod_image_name = img_url.split("/")[-1]
                    image_path = 'banner/images/'+mod_image_name

                    image_upload = Banner(
                        banner_image=image_path,
                        banner_name=banName.sub_category_name,
                        banner_link=link)
                    image_upload.save()
                messages.success(request, ' Banner Upload Successfull')
                return redirect('admin_login:banner:banner_list')
















            # website logo
            if 'header_logo' in request.FILES:
                print('hi')
                print('hi')
                print('hi')
                print('hi')
                print('hi')
                print('hi')
                print('hi')
                print('hi')
                logo = request.FILES['header_logo']
                print()
                print()
                print()
                print(logo)
                print()
                print()
                print()
                print()
                logosave = webLogo.objects.update_or_create(banner_name='weblogo',defaults={'banner_image':logo})
           
                
                # banimgObj = webLogo.objects.get(banner_name='header_logo')
                # banner_link = request.POST.getlist('banner_link')
                # men_banner_image = request.FILES.getlist('header_logo')
                # for image, link in zip(men_banner_image, banner_link):
                #     print (image)
                #     # print (link)
                #     fs = FileSystemStorage()
                #     image_title = "website_header_logo." + image.name.split(".")[-1]
                #     upload_image = fs.save(
                #         "banner/website/header_logo/" + image_title, image)
                #     img_url = fs.url(upload_image)
                #     mod_image_name = img_url.split("/")[-1]
                #     image_path = 'banner/website/header_logo/' + mod_image_name

                #     image_upload = Banner(banner_image=image_path, banner_name='header_logo', banner_link=link)
                #     banimgObj.banner_image =image_path
                #     banimgObj.banner_link = link
                #     banimgObj.save()
                messages.success(request,'Website header logo Upload Successfull')
                return redirect('admin_login:banner:banner_list')


            if 'footer_logo' in request.FILES:
                banner_link = request.POST.getlist('banner_link')
                men_banner_image = request.FILES.getlist('footer_logo')
                for image, link in zip(men_banner_image, banner_link):
                    print (image)
                    # print (link)
                    fs = FileSystemStorage()
                    image_title = "website_footer_logo." + image.name.split(".")[-1]
                    upload_image = fs.save("banner/website/footer_logo/" + image_title, image)
                    img_url = fs.url(upload_image)
                    mod_image_name = img_url.split("/")[-1]
                    image_path = 'banner/website/footer_logo/' + mod_image_name

                    image_upload = Banner(banner_image=image_path,banner_name='footer_logo',banner_link=link)
                    image_upload.save()
                messages.success(request,'Website footer logo Upload Successfull')
                return redirect('admin_login:banner:banner_list')




















            if 'advatice_1' in request.FILES:
                banner_link = request.POST.getlist('banner_link')
                men_banner_image = request.FILES.getlist('advatice_1')
                for image, link in zip(men_banner_image, banner_link):
                    # print (image)
                    # print (link)
                    fs = FileSystemStorage()
                    image_title = "advatice-1-banner."+image.name.split(".")[-1]
                    upload_image = fs.save("banner/advatice1/images/"+image_title, image)
                    img_url = fs.url(upload_image)
                    mod_image_name = img_url.split("/")[-1]
                    image_path = 'banner/advatice1/images/'+mod_image_name

                    image_upload = adactive(banner_image=image_path, banner_name='advatice_1', banner_link=link)
                    image_upload.save()
                messages.success(request, 'Advatice Banner 1 Upload Successfull')
                return redirect('admin_login:banner:banner_list')

            if 'advatice_2' in request.FILES:
                banner_link = request.POST.getlist('banner_link')
                men_banner_image = request.FILES.getlist('advatice_2')
                for image, link in zip(men_banner_image, banner_link):
                    # print (image)
                    # print (link)
                    fs = FileSystemStorage()
                    image_title = "advatice-2-banner."+image.name.split(".")[-1]
                    upload_image = fs.save("banner/advatice2/images/"+image_title, image)
                    img_url = fs.url(upload_image)
                    mod_image_name = img_url.split("/")[-1]
                    image_path = 'banner/advatice2/images/'+mod_image_name

                    image_upload = adactive(banner_image=image_path,
                                            banner_name='advatice_2',
                                            banner_link=link)
                    image_upload.save()
                messages.success(request, 'Advatice Banner 2 Upload Successfull')
                return redirect('admin_login:banner:banner_list')

            if 'advatice_3' in request.FILES:
                banner_link = request.POST.getlist('banner_link')
                men_banner_image = request.FILES.getlist('advatice_3')
                for image, link in zip(men_banner_image, banner_link):
                    # print (image)
                    # print (link)
                    fs = FileSystemStorage()
                    image_title = "advatice-3-banner."+image.name.split(".")[-1]
                    upload_image = fs.save("banner/advatice3/images/"+image_title, image)
                    img_url = fs.url(upload_image)
                    mod_image_name = img_url.split("/")[-1]
                    image_path = 'banner/advatice3/images/'+mod_image_name

                    image_upload = adactive(banner_image=image_path, banner_name='advatice_3', banner_link=link)
                    image_upload.save()
                messages.success(request, 'Advatice Banner 3 Upload Successfull')
                return redirect('admin_login:banner:banner_list')

            if 'advatice_4' in request.FILES:
                banner_link = request.POST.getlist('banner_link')
                men_banner_image = request.FILES.getlist('advatice_4')
                for image, link in zip(men_banner_image, banner_link):
                    # print (image)
                    # print (link)
                    fs = FileSystemStorage()
                    image_title = "advatice-4-banner."+image.name.split(".")[-1]
                    upload_image = fs.save("banner/advatice4/images/"+image_title, image)
                    img_url = fs.url(upload_image)
                    mod_image_name = img_url.split("/")[-1]
                    image_path = 'banner/advatice4/images/'+mod_image_name

                    image_upload = adactive(banner_image=image_path, banner_name='advatice_4', banner_link=link)
                    image_upload.save()
                messages.success(request, 'Advatice Banner 4 Upload Successfull')
                return redirect('admin_login:banner:banner_list')

            if 'advatice_5' in request.FILES:
                banner_link = request.POST.getlist('banner_link')
                men_banner_image = request.FILES.getlist('advatice_5')
                for image, link in zip(men_banner_image, banner_link):
                    # print (image)
                    # print (link)
                    fs = FileSystemStorage()
                    image_title = "advatice-5-banner."+image.name.split(".")[-1]
                    upload_image = fs.save("banner/advatice5/images/"+image_title, image)
                    img_url = fs.url(upload_image)
                    mod_image_name = img_url.split("/")[-1]
                    image_path = 'banner/advatice5/images/'+mod_image_name

                    image_upload = adactive(banner_image=image_path, banner_name='advatice_5', banner_link=link)
                    image_upload.save()
                messages.success(request, 'Advatice Banner 5 Upload Successfull')
                return redirect('admin_login:banner:banner_list')

            if 'advatice_6' in request.FILES:
                banner_link = request.POST.getlist('banner_link')
                men_banner_image = request.FILES.getlist('advatice_6')
                for image, link in zip(men_banner_image, banner_link):
                    # print (image)
                    # print (link)
                    fs = FileSystemStorage()
                    image_title = "advatice-6-banner."+image.name.split(".")[-1]
                    upload_image = fs.save("banner/advatice6/images/"+image_title, image)
                    img_url = fs.url(upload_image)
                    mod_image_name = img_url.split("/")[-1]
                    image_path = 'banner/advatice6/images/'+mod_image_name

                    image_upload = adactive(banner_image=image_path, banner_name='advatice_6', banner_link=link)
                    image_upload.save()
                messages.success(request, 'Advatice Banner 6 Upload Successfull')
                return redirect('admin_login:banner:banner_list')

            if 'advatice_right' in request.FILES:
                banner_link = request.POST.getlist('banner_link')
                men_banner_image = request.FILES.getlist('advatice_right')
                for image, link in zip(men_banner_image, banner_link):
                    # print (image)
                    # print (link)
                    fs = FileSystemStorage()
                    image_title = "advatice-right-banner."+image.name.split(".")[-1]
                    upload_image = fs.save("banner/advatice_right/images/"+image_title, image)
                    img_url = fs.url(upload_image)
                    mod_image_name = img_url.split("/")[-1]
                    image_path = 'banner/advatice_right/images/'+mod_image_name

                    image_upload = adactive(banner_image=image_path, banner_name='advatice_right', banner_link=link)
                    image_upload.save()
                messages.success(request, 'Advatice Banner Right Upload Successfull')
                return redirect('admin_login:banner:banner_list')

            if 'advatice_left' in request.FILES:
                banner_link = request.POST.getlist('banner_link')
                men_banner_image = request.FILES.getlist('advatice_left')
                for image, link in zip(men_banner_image, banner_link):
                    # print (image)
                    # print (link)
                    fs = FileSystemStorage()
                    image_title = "advatice-right-banner."+image.name.split(".")[-1]
                    upload_image = fs.save("banner/advatice_left/images/"+image_title, image)
                    img_url = fs.url(upload_image)
                    mod_image_name = img_url.split("/")[-1]
                    image_path = 'banner/advatice_left/images/'+mod_image_name

                    image_upload = adactive(banner_image=image_path, banner_name='advatice_left', banner_link=link)
                    image_upload.save()
                messages.success(request, 'Advatice Banner Left Upload Successfull')
                return redirect('admin_login:banner:banner_list')

            # *******************************   Banner title    ***********************************************
            # print (request.POST)
            # return
            # if 'men_banner_title' in request.POST:
            #     banner_custom_title = request.POST.getlist('men_banner_title')
            #     if banner_custom_title[0] != "":
            #         edit_banner_custom_title = Banner.objects.filter(banner_name='men_banner').update(banner_name_custom=banner_custom_title[0])
            # if 'women_banner_title' in request.POST:
            #     banner_custom_title = request.POST.getlist('women_banner_title')
            #     if banner_custom_title[0] != "":
            #         edit_banner_custom_title = Banner.objects.filter(banner_name='women_banner').update(banner_name_custom=banner_custom_title[0])
            # if 'baby_kid_banner_title' in request.POST:
            #     banner_custom_title = request.POST.getlist('baby_kid_banner_title')
            #     if banner_custom_title[0] != "":
            #         edit_banner_custom_title = Banner.objects.filter(banner_name='baby_kid_banner').update(banner_name_custom=banner_custom_title[0])
            # if 'mobile_banner_title' in request.POST:
            #     banner_custom_title = request.POST.getlist('mobile_banner_title')
            #     if banner_custom_title[0] != "":
            #         edit_banner_custom_title = Banner.objects.filter(banner_name='mobile_banner').update(banner_name_custom=banner_custom_title[0])

            # if 'electronic_banner_title' in request.POST:
            #     banner_custom_title = request.POST.getlist('electronic_banner_title')
            #     if banner_custom_title[0] != "":
            #         edit_banner_custom_title = Banner.objects.filter(banner_name='electronic_banner').update(banner_name_custom=banner_custom_title[0])

            # if 'office_appliance_banner_title' in request.POST:
            #     banner_custom_title = request.POST.getlist('office_appliance_banner_title')
            #     if banner_custom_title[0] != "":
            #         edit_banner_custom_title = Banner.objects.filter(banner_name='office_appliance_banner').update(banner_name_custom=banner_custom_title[0])

            # *******************************   Banner title    ***********************************************
        except Exception as e:
            print (e)

        context = self.get_context_data()
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = dict()
        seller_id = self.kwargs.get('seller_id')
        get_name = zaptayadmin.objects.all().get(email_id=self.request.session['admin_email_id'])

        cat = MainCategory.objects.get(main_category_name='featured')
        print(cat)
        sucat = SubCategory.objects.filter(category_id = cat)
        print(sucat)


        baners = Banner.objects.all().values('id', 'banner_image', 'banner_link', 'banner_id', 'banner_name_custom','banner_name')
        # get_womens_fashion = Banner.objects.filter(banner_name='women_banner').values('id', 'banner_image', 'banner_link', 'banner_id', 'banner_name_custom')
        # get_baby_kid_fashion = Banner.objects.filter(banner_name='baby_kid_banner').values('id', 'banner_image', 'banner_link', 'banner_id', 'banner_name_custom')
        # get_mobile_fashion = Banner.objects.filter(banner_name='mobile_banner').values('id', 'banner_image', 'banner_link', 'banner_id', 'banner_name_custom')
        # get_electronic_fashion = Banner.objects.filter(banner_name='electronic_banner').values('id', 'banner_image', 'banner_link', 'banner_id', 'banner_name_custom')
        # get_office_appliance_fashion = Banner.objects.filter(banner_name='office_appliance_banner').values('id', 'banner_image', 'banner_link', 'banner_id', 'banner_name_custom')

        get_advatice_banner_1 = adactive.objects.filter(banner_name='advatice_1').values('id', 'banner_image', 'banner_link', 'banner_id')
        get_advatice_banner_2 = adactive.objects.filter(banner_name='advatice_2').values('id', 'banner_image', 'banner_link', 'banner_id')
        get_advatice_banner_3 = adactive.objects.filter(banner_name='advatice_3').values('id', 'banner_image', 'banner_link', 'banner_id')
        get_advatice_banner_4 = adactive.objects.filter(banner_name='advatice_4').values('id', 'banner_image', 'banner_link', 'banner_id')
        get_advatice_banner_5 = adactive.objects.filter(banner_name='advatice_5').values('id', 'banner_image', 'banner_link', 'banner_id')
        get_advatice_banner_6 = adactive.objects.filter(banner_name='advatice_6').values('id', 'banner_image', 'banner_link', 'banner_id')

        get_advatice_banner_right = adactive.objects.filter(banner_name='advatice_right').values('id', 'banner_image', 'banner_link', 'banner_id')
        get_advatice_banner_left = adactive.objects.filter(banner_name='advatice_left').values('id', 'banner_image', 'banner_link', 'banner_id')

        context = {
            "page_name": "banner",
            "admin_name": get_name.admin_f_name + " " + get_name.admin_f_name,
            'Banner': baners,
            # 'women_fashion_image': get_womens_fashion,
            # 'baby_kid_fashion_image': get_baby_kid_fashion,
            # 'mobile_image': get_mobile_fashion,
            # 'electronic_image': get_electronic_fashion,
            # 'office_appliance_image': get_office_appliance_fashion,
            'advatice_banner_1_image': get_advatice_banner_1,
            'advatice_banner_2_image': get_advatice_banner_2,
            'advatice_banner_3_image': get_advatice_banner_3,
            'advatice_banner_4_image': get_advatice_banner_4,
            'advatice_banner_5_image': get_advatice_banner_5,
            'advatice_banner_6_image': get_advatice_banner_6,
            'advatice_banner_right_image': get_advatice_banner_right,
            'advatice_banner_left_image': get_advatice_banner_left,
            'frm': addBanner(),
            'sub_category': sucat,
        }
        return context

class WebSiteLogo(TemplateView):
    template_name = 'admin_template/website_logo/website_logo.html'

    def dispatch(self, request, *args, **kwargs):
        try:
            resp = request.session['admin_email_id']
            return super(WebSiteLogo, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)
            # return redirect('/site-admin/seller/seller-view/')
            return redirect('admin_login:admin_loginpage')

    def post(self, request, *args, **kwargs):
        try:
            if 'header_logo' in request.FILES:
                banner_link = request.POST.getlist('banner_link')
                men_banner_image = request.FILES.getlist('header_logo')
                for image, link in zip(men_banner_image, banner_link):
                    # print (image)
                    # print (link)
                    fs = FileSystemStorage()
                    image_title = "website_header_logo."+image.name.split(".")[-1]
                    upload_image = fs.save("banner/website/header_logo/"+image_title, image)
                    img_url = fs.url(upload_image)
                    mod_image_name = img_url.split("/")[-1]
                    image_path = 'banner/website/header_logo/'+mod_image_name

                    image_upload = Banner(banner_image=image_path, banner_name='header_logo', banner_link=link)
                    image_upload.save()
                messages.success(request, 'Website header logo Upload Successfull')
                return redirect('/site-admin/banner/website-logo/')

            if 'footer_logo' in request.FILES:
                banner_link = request.POST.getlist('banner_link')
                men_banner_image = request.FILES.getlist('footer_logo')
                for image, link in zip(men_banner_image, banner_link):
                    # print (image)
                    # print (link)
                    fs = FileSystemStorage()
                    image_title = "website_footer_logo."+image.name.split(".")[-1]
                    upload_image = fs.save("banner/website/footer_logo/"+image_title, image)
                    img_url = fs.url(upload_image)
                    mod_image_name = img_url.split("/")[-1]
                    image_path = 'banner/website/footer_logo/'+mod_image_name

                    image_upload = Banner(banner_image=image_path, banner_name='footer_logo', banner_link=link)
                    image_upload.save()
                messages.success(request, 'Website footer logo Upload Successfull')
                return redirect('/site-admin/banner/website-logo/')
        except Exception as e:
            print (e)

        context = self.get_context_data()
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = dict()
        seller_id = self.kwargs.get('seller_id')
        get_name = zaptayadmin.objects.all().get(email_id=self.request.session['admin_email_id'])

        get_header_logo = Banner.objects.filter(banner_name='header_logo').values('id', 'banner_image', 'banner_link', 'banner_id')
        get_footer_logo = Banner.objects.filter(banner_name='footer_logo').values('id', 'banner_image', 'banner_link', 'banner_id')

        context = {"page_name": "logo",
                    "admin_name": get_name.admin_f_name+" "+get_name.admin_f_name,
                    "get_header_logo": get_header_logo,
                    "get_footer_logo": get_footer_logo,
                }
        return context

# ******************************************************************************************************************
# Ajax hendel

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse
import os

@csrf_exempt
def DeleteBannerImage(request):
    image_id = request.POST['image_id']

    bann = Banner.objects.get(banner_id=image_id)
    if bann == '':
        bannad = adactive.objects.get(banner_id=image_id)
        del_img = bannad
    else:
        del_img = bann
    del_img.delete()
    # del_image_path = Banner.objects.get(pk=image_id)
    # print (del_image_path.banner_image)
    os.remove('media/'+str(del_img.banner_image))

    data = {
        'status': 'success',
    }
    return JsonResponse(data)


@csrf_exempt
def DeleteadBannerImage(request):
    image_id = request.POST['image_id']

    del_img = adactive.objects.get(banner_id=image_id)

    del_img.delete()
    # del_image_path = Banner.objects.get(pk=image_id)
    # print (del_image_path.banner_image)
    os.remove('media/' + str(del_img.banner_image))

    data = {
        'status': 'success',
    }
    return JsonResponse(data)
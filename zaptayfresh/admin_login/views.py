from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, TemplateView, FormView

from .login_forms import LoginForm , ResetPwd
from .models import zaptayadmin

from django.core.mail import EmailMessage

from django.contrib.auth import logout
# Create your views here.


########################################################## Admin Login ############################################################################

class ShowadminLogin(FormView):
    form_class = LoginForm
    template_name = 'admin_templates/admin_login_Templates/admin_login.html'
    success_url = 'dashboard'

    def post(self, request, *args, **kwargs):
        UloginForm = self.get_form()

        if UloginForm.is_valid():
            try:
                Uemail_id = UloginForm.cleaned_data['email_id']
                print(Uemail_id)# print
                Upwd = UloginForm.cleaned_data['password']
                print(Upwd)

                session_data = zaptayadmin.objects.all().get(email_id=Uemail_id, password=Upwd)
                print('session data variable')# print
                print(session_data.email_id)
                print(session_data.password)
                
                #session set
                request.session['admin_email_id'] = session_data.email_id
                request.session.set_expiry(0)
                print('session set done!')  # print
                

                return self.form_valid(UloginForm)
            except Exception as e:
                print(e) 
                context = {"db_error": "User Not Exist", 'form': UloginForm}
                return self.render_to_response(context)
        else:
            return self.form_invalid(UloginForm)



 

    
############################################## Dash Board ############################################################################
class DashBoard(TemplateView):
    template_name = 'admin_templates/admin_login_Templates/admin_dashboard.html'

    def dispatch(self, request, *args, **kwargs):
        
        try:  
            resp = request.session['admin_email_id']
            if resp is None:
                print('session dose not matched for dashboard')# print
            else:
                print('session matched for dashboard')# print
            return super(DashBoard, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)
            return redirect('admin_login:admin_loginpage')
    
    def get_context_data(self, **kwargs):
        
        get_name = zaptayadmin.objects.all().get(email_id=self.request.session['admin_email_id'])
        context = dict()
        context = {"page_name": "dashboard", "admin_name": get_name.admin_f_name+" "+get_name.admin_l_name}
        return context



###################################################### Log Out #################################################################
""" class logoutUser(TemplateView):
    template_name = 'admin_templates/admin_login_Templates/admin_login.html'
    def dispatch(self, request, *args, **kwargs):
        try:
            logout(request)
            del ()
            print('User Loged out')# print
            return redirect('admin_login:admin_loginpage')
        except Exception as e:
            print('except')
            print(e)
            return redirect('admin_login:admin_loginpage')

 """

def Logout(request):
    logout(request)
    return redirect('admin_login:admin_loginpage')



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







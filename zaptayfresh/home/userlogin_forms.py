from django import forms

import re


class SignUpForm(forms.Form):
    user_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control form-control-user", 'id': "exampleInputUFname", 'placeholder': "User Full Name"}), error_messages={'required': 'First Name required'})
    email_id = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control form-control-user', 'id': 'exampleInputEmail', 'aria-describedby':"emailHelp", 'placeholder':"Enter Email Address..."}), error_messages={'required': 'Email Id Required'})
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control form-control-user", 'id': "exampleInputPassword", 'placeholder': "Password"}), error_messages={'required': 'Password Required'})
    phone_no = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control form-control-user", 'id': "exampleInputPassword", 'placeholder': "Phone Number"}), error_messages={'required': 'Phone Number Required'})

class LoginForm(forms.Form):
    email_id = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control form-control-user', 'id': 'exampleInputEmail', 'aria-describedby':"emailHelp", 'placeholder':"Enter Email Address..."}), error_messages={'required': 'Email Id Required'})
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control form-control-user", 'id': "exampleInputPassword", 'placeholder': "Password"}), error_messages={'required': 'Password Required'})


class ResetPwd(forms.Form):
    email_id_forReset = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control form-control-user', 'id': 'exampleInputEmail', 'aria-describedby':"emailHelp", 'placeholder':"Enter Registered Email Address..."}), error_messages={'required': 'Registered Email Id Required'})


class PwdResetFrm(forms.Form):
    email_id_forReset = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control form-control-user', 'id': 'exampleInputEmail', 'aria-describedby':"emailHelp", 'placeholder':"Enter Registered Email Address..."}), error_messages={'required': 'Registered Email Id Required'})

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class RegistrationForm(UserCreationForm):
    email=forms.EmailField(required=True)

    class Meta:
        model=User
        fields=(
            'username',
            'email',
            'id',
            'password'
        )
    def save(self,commit=False):
        user=super(RegistrationForm,self).save(commit=False)
        # user.username=self.cleaned_data['username']
        user.email=self.cleaned_data['email']
        user.phone=self.cleaned_data['phone']
        
        if commit:
            user.save()

        return user
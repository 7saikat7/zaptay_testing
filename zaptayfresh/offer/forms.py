from django import forms
from offer.models import *


class OfferSelect(forms.Form):
    OfferChoise = forms.ModelChoiceField(queryset=Offer.objects.all(),widget=forms.Select(attrs={'class': 'form-control', 'id': 'OfferChoise', 'placeholder': 'Select The Deals'}), error_messages={'required': 'Sub Category Required'})
    OfferPrice = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'youtube', 'placeholder': 'Offer Price'}))
   

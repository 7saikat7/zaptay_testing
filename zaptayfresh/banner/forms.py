from django import forms
from attribute.models import *



class addBanner(forms.Form):
    hola = [
        ('','Banners Empty'),
        ('', '1')
        ]
    try:
        lat =  MainCategory.objects.get(main_category_name='featured')
        cat = SubCategory.objects.filter(category_id = lat)
    
    except Exception as e:
        cat = ''
 

    if cat != '':
        Banner_category = forms.ModelChoiceField(queryset=cat,widget=forms.Select(attrs={'class': 'form-control', 'id': 'Banner_category', 'name':'Banner_category'}), error_messages={'required': 'Main Category Required'})
    else:
        Banner_category = forms.CharField(widget=forms.Select(choices=hola,attrs={'class': 'form-control', 'id': 'Banner_category', 'name':'Banner_category'}), error_messages={'required': 'Main Category Required'})

from django import forms
from seller.models import *
from attribute.models import *



def getsize():
    allsiz = Size.objects.values('size_name')
    siz_list = list()
    for i in allsiz:
        siz = (i['size_name'].upper(), i['size_name'].upper())
        siz_list.append(siz)

    return siz_list


class ProductForm(forms.Form):





    product_title       = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'product_title', 'placeholder': 'Title of the product'}), error_messages={'required': 'Product Title Required'})

    category            = forms.ModelChoiceField(queryset=MainCategory.objects.all(),widget=forms.Select(attrs={'class': 'form-control', 'id': 'category', 'placeholder': 'Select The Deals'}), error_messages={'required': 'Sub Category Required'})
    sub_category       = forms.ModelChoiceField(queryset=SubCategory.objects.all(),widget=forms.Select(attrs={'class': 'form-control', 'id': 'SubCategory', 'placeholder': 'Select The Deals'}), error_messages={'required': 'Sub Category Required'})
    tertiary            = forms.ModelChoiceField(queryset=TertiaryCategory.objects.all(),widget=forms.Select(attrs={'class': 'form-control', 'id': 'TertiaryCategory', 'placeholder': 'Select The Deals'}), error_messages={'required': 'Sub Category Required'})
    under_tertiary      = forms.ModelChoiceField(queryset=UnderTertiaryCategory.objects.all(),widget=forms.Select(attrs={'class': 'form-control', 'id': 'UnderTertiaryCategory', 'placeholder': 'Select The Deals'}), error_messages={'required': 'Sub Category Required'})


    seller              = forms.ModelChoiceField(queryset=Seller.objects.all(),widget=forms.Select(attrs={'class': 'form-control', 'id': 'selectseller', 'placeholder': 'Select The Deals'}), error_messages={'required': 'Sub Category Required'})
    made_in             = forms.ModelChoiceField(queryset=MadeIn.objects.all(),widget=forms.Select(attrs={'class': 'form-control', 'id': 'madein', 'placeholder': 'Select The Deals'}), error_messages={'required': 'Sub Category Required'})
    brand               = forms.ModelChoiceField(queryset=Brand.objects.all(),widget=forms.Select(attrs={'class': 'form-control', 'id': 'brand', 'placeholder': 'Select The Deals'}), error_messages={'required': 'Sub Category Required'})

    description         = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'descrip', 'rows': 11, 'placeholder': 'Product description'}))

    same_day_delivary_check     = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'custom-control-input', 'id': 'same_day_delivary'}))
    same_day_delivary_price     = forms.CharField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'inputAddress', 'placeholder': 'Price', 'min': 0}))

    next_day_delivary_check     = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'custom-control-input', 'id': 'next_day_delivary'}))
    next_day_delivary_price     = forms.CharField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'inputAddress', 'placeholder': 'Price', 'min': 0}))

    customize_delivary_check    = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'custom-control-input', 'id': 'customize_day_delivary'}))
    customize_delivary_day      = forms.CharField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'inputAddress', 'placeholder': 'Add Day', 'min': 0}))
    customize_delivary_price    = forms.CharField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'inputAddress', 'placeholder': 'Price', 'min': 0}))

    cod                          = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'custom-control-input', 'id': 'cod'}))
    return_product              = forms.BooleanField(required=True, widget=forms.CheckboxInput(attrs={'class': 'custom-control-input', 'id': 'returnn','checked':True}))

    AddToOffer                  = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'custom-control-input', 'id': 'AddToOffer'}))

    B2b_check                   = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'custom-control-input', 'id': 'B2b'}))



    size                    = forms.MultipleChoiceField(choices=getsize(), widget=forms.SelectMultiple(attrs={'id': 'chkveg'}),required=False, label='size')


  

    main_price                  = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'mrp', 'placeholder': 'Main Price', 'min': 0}), error_messages={'required': 'Main Price Required'})
    offer_price                 = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'sell', 'placeholder': 'Offer Price', 'min': 0}), error_messages={'required': 'Offer Price Required'})

    color                       = forms.ModelChoiceField(queryset=Colour.objects.all(),widget=forms.Select(attrs={'class': 'form-control', 'id': 'color', 'placeholder': 'Select The Deals'}), error_messages={'required': 'Sub Category Required'})



    stock_entry                 = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'stock', 'placeholder': 'Stock Entry', 'min': 0}), error_messages={'required': 'Purchase Price Required'})



    youtube                     = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'youtube', 'placeholder':'Youtube link'}))
    stock                       = forms.CharField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'stock', 'placeholder': 'Stock', 'min': 0}))
    product_image               = forms.ImageField(required=True, widget=forms.FileInput(attrs={'class': 'custom-file-input', 'id': 'product_img', 'multiple': 'multiple'}))



    def clean(self):
        product_desc = self.cleaned_data.get('description')

        if product_desc == "" or len(product_desc) < 5:
            print("Error")
            raise forms.ValidationError(
                ({'description': ["Product Description Required"]})
            )
        return True


class ProductImageForm(forms.Form):

  

    prod_idimg             = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'product_idimg', 'placeholder': 'Enter Id'}), error_messages={'required': 'Product Title Required'})
    product_titlee          = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'product_title', 'placeholder': 'Title of the product'}), error_messages={'required': 'Product Title Required'})
    colorimg               = forms.ModelChoiceField(required=False,queryset=Colour.objects.all(),widget=forms.Select(attrs={'class': 'form-control', 'id': 'colorimg', 'placeholder': 'Select The Deals'}), error_messages={'required': 'Sub Category Required'})
    youtubeimg             = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'youtubeimg', 'placeholder':'Youtube link'}))
    stockimg               = forms.CharField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'stockimg', 'placeholder': 'Price', 'min': 0}))
    product_imageimg        = forms.ImageField(required=True, widget=forms.FileInput(attrs={'class': 'custom-file-input', 'id': 'product_img2', 'multiple': 'multiple'}))
    main_priceimg          = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'mrp', 'placeholder': 'Main Price', 'min': 0}), error_messages={'required': 'Main Price Required'})
    sell_priceimg          = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'sell', 'placeholder': 'Sell Price', 'min': 0}), error_messages={'required': 'Main Price Required'})
    sizeimg                    = forms.MultipleChoiceField(choices=getsize(), widget=forms.SelectMultiple(attrs={'id': 'chkvegimg'}),required=False, label='size')
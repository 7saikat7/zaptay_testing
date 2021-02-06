from django import forms
from attribute.models import *



class AddMainCategoryForm(forms.Form):
    category_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'id': 'exampleInputEmail', 'aria-describedby':"emailHelp", 'placeholder':"Example: Men fashion, Women fashion"}), error_messages={'required': 'Category name required'})


def get_main_category():
    main_category = MainCategory.objects.all().values('category_id', 'main_category_name')
    # print (main_category[0].category_id, main_category[0].main_category_name)
    main_cat_list = list()
    for data in main_category:
        cat_data = (data['category_id'], data['main_category_name'])
        main_cat_list.append(cat_data)
    return main_cat_list

class AddSubCategoryForm(forms.Form):

    CATEGORY_CHOOSE = get_main_category()

    category_list = forms.CharField(label='What is your favorite fruit?', widget=forms.Select(choices=CATEGORY_CHOOSE, attrs={'class': 'my_select_box'}))
    sub_category_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'id': 'exampleInputEmail', 'aria-describedby':"emailHelp", 'placeholder':"Example: Saree, Kurta"}), error_messages={'required': 'Category name required'})

class MainCategoryForm(forms.Form):
    category_add_form = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'id': 'exampleInputEmail', 'aria-describedby':"emailHelp", 'placeholder':"Category"}), error_messages={'required': 'Category name required'})

def get_main_category():
    main_category = MainCategory.objects.all().values('category_id', 'main_category_name')
    main_cat_list = list()
    initial = ('', 'Select category')
    main_cat_list.append(initial)
    for data in main_category:
        cat_data = (data['category_id'], data['main_category_name'])
        main_cat_list.append(cat_data)
    return main_cat_list



################################################# used #######################################################################
class CategoryForm(forms.Form):
    category_add_form = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'id': 'exampleInputEmail', 'aria-describedby':"emailHelp", 'placeholder':"Category"}), error_messages={'required': 'Category name required'})

 
class SubcategoryForm(forms.Form):
    category_list = forms.ModelChoiceField(queryset=MainCategory.objects.all(),widget=forms.Select(attrs={'class': 'form-control', 'id': 'category_list'}), error_messages={'required': 'Main Category Required'})
    sub_category_add_form = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'aria-describedby':"emailHelp", 'placeholder':"Sub category"}), error_messages={'required': 'Sub Category name required'})


class TertiaryCategoryForm(forms.Form):
    sub_category_list = forms.ModelChoiceField(queryset=SubCategory.objects.all(),widget=forms.Select(attrs={'class': 'form-control', 'id': 'category_list'}), error_messages={'required': 'Main Category Required'})
    tert_category_add_form = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'aria-describedby':"emailHelp", 'placeholder':"Tertiary Category"}), error_messages={'required': 'Sub Category name required'})


class UnderTertiaryCategoryForm(forms.Form):
    tert_category_list = forms.ModelChoiceField(queryset=TertiaryCategory.objects.all(),widget=forms.Select(attrs={'class': 'form-control', 'id': 'category_list'}), error_messages={'required': 'Main Category Required'})
    under_tert_category_add_form = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'aria-describedby':"emailHelp", 'placeholder':"Under Tertiary Category"}), error_messages={'required': 'Under Tertiary Category name required'})


class BrandForm(forms.Form):
    brand_add_form = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'aria-describedby':"emailHelp", 'placeholder':"Brand name"}), error_messages={'required': 'Brand name required'})


class ColorForm(forms.Form):
    color_add_form = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'aria-describedby':"emailHelp", 'placeholder':"Colour name"}), error_messages={'required': 'Color name required'})


class SizeForm(forms.Form):
    size_add_form = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'aria-describedby':"emailHelp", 'placeholder':"Size"}), error_messages={'required': 'Color name required'})


class MadeInForm(forms.Form):
    source_add_form = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'aria-describedby':"emailHelp", 'placeholder':"Source"}), error_messages={'required': 'Color name required'})


class SameDayPincodeForm(forms.Form):
    same_day_pin_add_form = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'aria-describedby':"emailHelp", 'placeholder':"Pincode"}), error_messages={'required': 'Pincode required'})


class NextDayPincodeForm(forms.Form):
    next_day_pin_add_form = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'aria-describedby':"emailHelp", 'placeholder':"Pincode"}), error_messages={'required': 'Pincode required'})
from django import forms

class SellerForm(forms.Form):
    seller_title = forms.CharField(widget=forms.TextInput(attrs={
                        'class':'form-control', 'id': 'seller_title', 'Placeholder': 'Seller Title'
                    }), error_messages={'required': 'Seller Title Required'})
    seller_name = forms.CharField(widget=forms.TextInput(attrs={
                        'class':'form-control', 'id': 'seller_name', 'Placeholder': 'Seller Name'
                    }), error_messages={'required': 'Seller Name Required'})
    seller_email = forms.CharField(widget=forms.EmailInput(attrs={
                        'class':'form-control', 'id': 'seller_email_id', 'Placeholder': 'Email Id'
                    }), error_messages={'required': 'Seller Email Id Required'})
    seller_phone_no = forms.CharField(required=False, widget=forms.NumberInput(attrs={
                        'class':'form-control', 'id': 'seller_ph_no', 'Placeholder': 'Phone No'
                    }))
    seller_address = forms.CharField(required=False, widget=forms.Textarea(attrs={
                        'class':'form-control', 'id':'seller_address', 'rows':'5', "placeholder":"Seller Address"
                    }), error_messages={'required': 'Seller Address Required'})
    seller_specification = forms.CharField(widget=forms.TextInput(attrs={
                        'class':'form-control', 'id': 'seller_specufication', 'Placeholder': 'Seller specification'
                    }), error_messages={'required': 'Seller Specification Required'})
    seller_gst_no = forms.CharField(required=False, widget=forms.TextInput(attrs={
                        'class':'form-control', 'id': 'gst_no', 'Placeholder': 'GST NO.'
                    }))
    seller_aadhaar_no = forms.CharField(required=False, widget=forms.TextInput(attrs={
                        'class':'form-control', 'id': 'aadhaar', 'Placeholder': 'Aadhaar No.'
                    }))
    seller_voter_no = forms.CharField(required=False, widget=forms.TextInput(attrs={
                        'class':'form-control', 'id': 'voter_no', 'Placeholder': 'Voter No.'
                    }))

    seller_img = forms.ImageField(required=False, widget=forms.FileInput(attrs={
                        'class':'custom-file-input', 'id': 'seller_img'
                    }))
    gst_img = forms.ImageField(required=False, widget=forms.FileInput(attrs={
                        'class':'custom-file-input', 'id': 'gst_img'
                    }))
    aadhaar_img = forms.ImageField(required=False, widget=forms.FileInput(attrs={
                        'class':'custom-file-input', 'id': 'aadhaar_img', 'multiple': 'multiple'
                    }))
    voter_img = forms.ImageField(required=False, widget=forms.FileInput(attrs={
                        'class':'custom-file-input', 'id': 'voter_img', 'multiple': 'multiple'
                    }))
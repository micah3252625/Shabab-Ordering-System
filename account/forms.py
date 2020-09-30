from django import forms
from order.models import Customer

class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=32, 
            widget=forms.PasswordInput(
                attrs={
                    'class':'form-control px-3',  'required': 'true', 'placeholder':'Confirm Password', 'id':'confirm_password' ,
                }
            ),
    )
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'salutation': forms.Select(
                attrs={
                    'class': 'browser-default custom-select px-3',
                }
            ),
            'first_name':forms.TextInput(
                attrs={
                    'class':'form-control px-3', 'placeholder':'First name',
                }
            ),
            'last_name':forms.TextInput(
                attrs={
                    'class':'form-control px-3', 'placeholder':'Last name', 
                }
            ),
            'street':forms.TextInput(
                attrs={
                    'class':'form-control px-3',  'required': 'true', 'placeholder':'*Street', 
                }
            ),
            'barangay':forms.TextInput(
                attrs={
                   'class':'form-control px-3',  'required': 'true', 'placeholder':'*Village/Barangay', 
                }
            ),
            'number':forms.TextInput(
                attrs={
                    'class':'form-control px-3',  'required': 'true', 'placeholder':'*Mobile Number', 
                }
            ),
            'email':forms.EmailInput(
                attrs={
                    'class':'form-control px-3',  'required': 'true', 'placeholder':'Email Address', 
                }
            ),
            'password':forms.PasswordInput(
                attrs={
                    'class':'form-control px-3',  'required': 'true', 'placeholder':'Password', 'id':'password',
                }
            ),

        } 

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            print("ERROR PASSWORD")
            raise forms.ValidationError(
                "Password does not match!"
            )
        else:
            print("VALID PASSWORD")
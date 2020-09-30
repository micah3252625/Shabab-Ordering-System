from django import forms
from order.models import Pizza,  Customer

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        
        fields = ('name', 'size', 'base_price')

        widgets = {
            'size': forms.Select(
                attrs={
                    'class':'form-control col-16 text-center',
                    'id': 'size',
                    }
                ),
        }

from django import forms

class DealerForm(forms.Form):

    rnc = forms.CharField(max_length=100)
    name = forms.CharField(max_length=100)
    direction = forms.CharField()
    phone = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)




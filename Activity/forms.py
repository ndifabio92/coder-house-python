from django import forms

class ActivityForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField()
from django import forms
from Activity.models import Activity

class PromotionForm(forms.Form):
    first_activity = forms.ModelChoiceField(
        queryset=Activity.objects.filter(is_active=True),  
        widget=forms.Select,
        label="Actividad 1"
    )
    second_activity = forms.ModelChoiceField(
        queryset=Activity.objects.filter(is_active=True),  
        widget=forms.Select,
        label="Actividad 2"
    )
    discount_price = forms.DecimalField(label="Precio Promocion")
    start_date = forms.DateField(
            label="Inicio Promocion",
            widget=forms.DateInput(
            attrs={'type': 'date'}
        )
    )
    end_date = forms.DateField(
            label="Fin Promocion",
            widget=forms.DateInput(
            attrs={'type': 'date'}
        )
    )
    is_active = forms.BooleanField(
        label="Activo"
    )
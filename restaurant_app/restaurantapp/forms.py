from django import forms
from django import forms
from restaurantapp.models import reservas
from django.core  import validators

class FormProyecto(forms.ModelForm):
    class Meta:
        model = reservas
        fields = '__all__'

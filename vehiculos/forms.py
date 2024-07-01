from django import forms

class BusquedaMotos(forms.Form):
    marca = forms.CharField(max_length=20, required=False)
from django import forms
from estoque.models import Local, Tipo, Fabricante, Componente
import django.apps

class ComponenteForm(forms.Form):
    class Meta:
        model = Componente
        fields = ['quantidade']

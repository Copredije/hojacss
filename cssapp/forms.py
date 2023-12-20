from django import forms

from .models import Acta

class ActaForm(forms.ModelForm):

    class Meta:
        model = Acta
        fields = ('coordinador','obra', 'ubicacion', 'fecha','texto','firmacss', 'firmacontrata')
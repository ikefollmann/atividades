from django import forms
from django.contrib.admin import widgets
from .models import Atividade

class AtivForm(forms.ModelForm):
    class Meta:
        model = Atividade
        fields = '__all__'
        widgets = {
            'data_inicial': forms.TextInput(attrs = {'placeholder': 'AAAA-MM-DD hh:mm:ss'}),
            'data_final': forms.TextInput(attrs = {'placeholder': 'AAAA-MM-DD hh:mm:ss'}),
        }
    def __init__(self, *args, **kwargs):
        super(AtivForm, self).__init__(*args, **kwargs)
        #self.fields['data_inicial'].widget = widgets.AdminSplitDateTime()
        #self.fields['data_final'].widget = widgets.AdminSplitDateTime()
        for campo in self.visible_fields():
            campo.field.widget.attrs['class'] = 'form-control'

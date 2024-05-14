from django import forms

class MainForm(forms.Form):

    type_of_metal = forms.ChoiceField()
    weight = forms.CharField(label='Толщина (мм)', max_length=6)
    width = forms.CharField(label='Ширина (мм)')
    city = forms.ChoiceField(label='Город доставки', max_length=100)
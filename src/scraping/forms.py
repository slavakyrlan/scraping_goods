from django import forms

from scraping.models import Warehouse, Device, Information


class FindForm(forms.Form):
    warehouse = forms.ModelChoiceField(queryset=Warehouse.objects.all(),
                                       to_field_name="slug", required=False,
                                       widget=forms.Select(attrs={'class':'form-control'}),
                                       label='Склад'
                                       )
    device = forms.ModelChoiceField(queryset=Device.objects.all(),
                                    to_field_name="slug", required=False,
                                    widget=forms.Select(attrs={'class':'form-control'}),
                                    label='Оборудование'
                                    )

class VForm(forms.ModelForm):
    warehouse = forms.ModelChoiceField(
        queryset=Warehouse.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Склад'
    )
    device = forms.ModelChoiceField(
        queryset=Device.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Оборудование'
    )
    url = forms.CharField(label='URL', widget=forms.URLInput(
        attrs={'class': 'form-control'}))
    title = forms.CharField(label='Название устройства', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    company = forms.CharField(label='Компания', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    description = forms.CharField(label='Описание',
                                  widget=forms.Textarea(
                                      attrs={'class': 'form-control'}))

    class Meta:
        model = Information
        fields = '__all__'
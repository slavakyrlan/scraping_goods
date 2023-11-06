from django import forms

from scraping.models import Warehouse, Device


class FindForm(forms.Form):
    warehouse = forms.ModelChoiceField(queryset=Warehouse.objects.all(),
                                       to_field_name="slug", required=False,
                                       widget=forms.Select(attrs={'class':'form-control'}))
    device = forms.ModelChoiceField(queryset=Device.objects.all(),
                                    to_field_name="slug", required=False,
                                    widget=forms.Select(attrs={'class':'form-control'}))
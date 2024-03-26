from django import forms
from django.forms import ModelForm
from .models import Item, Business

#add item form
class  ItemModelForm(ModelForm):
    class Meta:
        model = Item
        fields=('item_name','price','photos',)


class BusinessForm(ModelForm):
    class Meta:
        model = Business
        fields = ['name', 'contact_details', 'location', 'description', 'logo', 'photos', 'videos']
        widgets = {
            'description': forms.Textarea(attrs={ 'rows': 5}),  
        }        
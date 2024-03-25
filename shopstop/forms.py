from django.forms import ModelForm
from .models import Item

#add item form
class  ItemModelForm(ModelForm):
    class Meta:
        model = Item
        fields=('item_name','price','photos',)
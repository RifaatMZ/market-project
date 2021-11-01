from .models import ItemDetail
from django import forms

class ItemDetailForm(forms.ModelForm):
    class Meta:
        model = ItemDetail
        fields = ['item', 'price', 'in_stock', 'quantity']
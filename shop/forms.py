from django import forms
from .models import Item, Account


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'


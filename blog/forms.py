from django.forms import ModelForm
from phonenumber_field.modelfields import PhoneNumberField
from .models import Order,Product
from django import forms


class OrderForm(ModelForm):
    class Meta:
        model = Order
        phone_number = PhoneNumberField()
        exclude=["product"]
        fields =["quantity","region"]
        widgets={
            "quantity": forms.TextInput(attrs={"class":"form-control"}),
           
            "region": forms.TextInput(attrs={"placeholder":"Arusha","class":"form-control"})
           
        }


class ProductForm(ModelForm):
    class Meta:
        
        model = Product
        exclude=["category"]
        fields=["name","price","image"]
    
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Weka Jina La Bati"}),
            "price": forms.TextInput(attrs={"class": "form-control", "placeholder": "Weka Bei"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }
        
        
       
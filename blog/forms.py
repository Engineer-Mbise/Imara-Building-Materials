from django.forms import ModelForm
from phonenumber_field.modelfields import PhoneNumberField
from .models import Order
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
        
        
       
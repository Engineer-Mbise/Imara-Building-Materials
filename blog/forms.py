from django.forms import ModelForm
from phonenumber_field.modelfields import PhoneNumberField
from .models import Order
from django import forms


class OrderForm(ModelForm):
    class Meta:
        model = Order
        phone_number = PhoneNumberField()
        exclude=["product","status"]
        fields =["quantity","customer_name","customer_phone_number","region"]
        widgets={
            "quantity": forms.TextInput(attrs={"class":"form-control"}),
            "customer_name": forms.TextInput(attrs={"placeholder":"John Doe","class":"form-control"}),
            "customer_phone_number":forms.TextInput(attrs={"placeholder":"0754xxxxxx","class":"form-control"}),
            "region": forms.TextInput(attrs={"placeholder":"Arusha","class":"form-control"})
           
        }
        
        
       
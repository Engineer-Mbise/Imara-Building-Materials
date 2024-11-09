from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import FileExtensionValidator
imageExt_validator=FileExtensionValidator(["JPG","PNG","GIF","TIFF","BMP","WEBP","HEIF","AVIF"])

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=250)
    description=models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name=models.CharField(max_length=250)
    price=models.TextField()
   
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/',validators=[imageExt_validator])
    
    def __str__(self):
        return self.name
    
    
class Order(models.Model):
    quantity = models.CharField(max_length=250)
    customer_name=models.CharField(max_length=250)
    region=models.CharField(max_length=250)
    customer_phone_number=PhoneNumberField()
    order_date=models.DateTimeField(auto_now_add=True)
    product=models.CharField(max_length=250)
    status=models.BooleanField(default=False)
    
    def __str__(self):
        return f"Order number {self.id} by {self.customer_name}"

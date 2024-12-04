from django.db import models
from authentication.models import User
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import FileExtensionValidator
from datetime import timedelta
from django.utils.timezone import now
imageExt_validator=FileExtensionValidator(["JPG","PNG","GIF","TIFF","BMP","WEBP","HEIF","AVIF"])

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=250)
    description=models.TextField(blank=True,null=True)
    
    class Meta:
      ordering = ['id']  
      
    def __str__(self):
        return self.name
    
    
    
class Product(models.Model):
    name=models.CharField(max_length=250)
    price=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/',validators=[imageExt_validator])
    
    class Meta:
      ordering = ['id']  
    
    def __str__(self):
        return self.name
      
      
    def get_absolute_url(self):
      
        return reverse('mabati') 
    
    
class Order(models.Model):
      class OrderStatus(models.TextChoices):
        PENDING = 'Inasubiri kuthibitishwa', 'Inasubiri kuthibitishwa'
        APPROVED = 'Imekamilika', 'Imekamilika'
        REJECTED = 'Imekataliwa', 'Imekataliwa'
      customer = models.ForeignKey(User,on_delete=models.CASCADE)
      quantity = models.CharField(max_length=250)
      region=models.CharField(max_length=250)
      product = models.CharField(max_length=250)
      status = models.CharField(max_length=200, choices=OrderStatus.choices, default=OrderStatus.PENDING)
      order_date = models.DateTimeField(auto_now_add=True)
      
      class Meta:
        ordering = ['id']  
        
        
      def __str__(self):
        return f"Order number {self.id} by {self.customer.first_name}"
    
      def can_cancel(self):
        return now() < self.order_date + timedelta(hours=24)
      
      def get_absolute_url(self):
        # Assuming you have a URL like "place_order/<str:name>"
         return reverse('place_order', args=[self.product])

from django.shortcuts import render,redirect
from .models import Product,Order
from .forms import OrderForm
from django.contrib import messages

# Create your views here.

def index(request):
    
    return render(request,"blog/index.html")


def mabati(request):
    
    bati=Product.objects.filter(category__name="Mabati")
    
    return render(request,"blog/mabati.html",{"bati":bati})



def place_order(request,name):
    if request.method=="POST":
        form=OrderForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.product=name
            instance.save()
            messages.info(request,"Umefanikiwa kuweka oda yako tutawasiliana na wewe na kuhakikisha mzigo wako unakufikia!!",extra_tags='oda')
            return redirect("index")
    else:
        form=OrderForm()
    return render(request,"blog/place_order.html",     {
            "customer_phone_number": form["customer_phone_number"],
            "customer_name": form["customer_name"],
            "quantity": form["quantity"],
            "region": form["region"],
            "name":name
          
        },)
    
 
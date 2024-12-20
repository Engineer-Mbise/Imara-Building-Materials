from django.shortcuts import render,redirect,get_object_or_404
from .models import Product,Order,Category
from .forms import OrderForm,ProductForm
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse



# Create your views here.

def index(request):
    
    return render(request,"blog/index.html")


def mabati(request):
      bati=Product.objects.filter(category__name="Mabati")
      if request.method == "POST":
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            mabati_category = get_object_or_404(Category, name="Mabati")
            instance.category = mabati_category
            instance.save()
            return redirect("mabati") 
        
      else: 
           form = ProductForm()
      return render(request,"blog/mabati.html",
        {
        "bati":bati,
        "name": form["name"],   
        "price": form["price"], 
        "image": form["image"],
        },
        )



def place_order(request,name):
    if not request.user.is_authenticated:
        request.session['original_url'] = request.get_full_path()
        return redirect('login')
        
    if request.method=="POST":
        form=OrderForm(request.POST)
           
        if form.is_valid():
            instance=form.save(commit=False)
            instance.product=name
            instance.customer=request.user
            instance.save()
            messages.info(request,"Umefanikiwa kuweka oda yako tutawasiliana na wewe na kuhakikisha mzigo wako unakufikia!!",extra_tags='oda')
            return redirect("index")
    else:
        form=OrderForm()
    return render(request,"blog/place_order.html",{
            
            "quantity": form["quantity"],
            "region": form["region"],
             "name":name
          
          
        },)
    

def my_orders(request):
     if not request.user.is_authenticated:
        request.session['original_url'] = request.get_full_path()
        return redirect('login')
    
     if request.user.role == 'ADMIN' or request.user.role == 'OWNER': 
        orders=Order.objects.all()
        
     else:
         
          orders=Order.objects.filter(customer=request.user)
          messages.info(request,"Baada ya masaa 24 kupita hautoweza kuondoa oda uliyoweka",extra_tags='oda_limit')
     return render(request,"blog/my_orders.html",{"orders":orders})
    
def wasifu(request):
    return render(request,"blog/wasifu.html")


def cancel_order(request,pk):
    order_to_be_canceled=Order.objects.filter(id=pk)
    order_to_be_canceled.delete()
    return redirect('my_orders')




def delete_product(request,product_name):
    product_to_be_deleted=Product.objects.filter(name=product_name)
    product_to_be_deleted.delete()
    return redirect('mabati')




def update_order_status(request, order_id):
    if request.method == 'POST':
        order = Order.objects.get(pk=order_id)
        order.status = request.POST['status']
        order.save()
        return redirect('my_orders') 
    
    
    
def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow: /admin/",
        "Disallow: /private/",
        "Allow: /static/",
        f"Sitemap: https://{request.get_host()}/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")





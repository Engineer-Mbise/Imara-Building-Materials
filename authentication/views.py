from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from django.urls import reverse
from .models import User
from .forms import RegistrationForm,UserEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

# Create your views here.


def registration(request):
   
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role='Customer'
            user.password = make_password(form.cleaned_data["password"])
            form.save()
            return redirect("login")     
    else:
        form=RegistrationForm()       
    return render(request,"authentication/registration.html",{
        "first_name":form['first_name'],
        "last_name":form["last_name"],
        "email":form["email"],
        "password":form["password"],
        "phone_number":form["phone_number"],
      
    })
    
    


def login_view(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
       
        user=authenticate(email=email,password=password)
        
        if user is not None:
            login(request,user)
            original_url = request.session.pop('original_url', None)
            if original_url:
                return redirect(original_url)
           
            return redirect(reverse("index"))
        else:
            return redirect("registration")
        
    else:
        return render(request,"authentication/login.html")





def user_logout(request):
 
    logout(request)
  
    return redirect('index')
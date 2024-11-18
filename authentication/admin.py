from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class UserAdmin(UserAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                    "phone_number",
                    "role",
                    "first_name",
            
                    "last_name",
                  
                 
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "first_name",
               
                    "last_name",
                
                    "phone_number",
                    "role",
               
                ),
            },
        ),
    )

    list_display = [
        "email",
        "first_name",
        "last_name",
      
        "phone_number",
        "role",
       
    ]

    search_fields = (
        "email",
        "first_name",
        "last_name",
        "phone_number",
        "role",
        "password",
     
       
    )

    list_filter = (
        "is_active",
        "is_staff",
        "is_superuser",
        "groups",
        "email",
    )

    ordering = ("id",)


admin.site.register(User, UserAdmin)


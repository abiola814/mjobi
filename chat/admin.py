from django.contrib import admin

# Register your models here.from django.contrib import admin
from .models import UserProfile, Message, Customers

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Message)
admin.site.register(Customers)

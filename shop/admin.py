from django.contrib import admin

# Register your models here.

from .models import Products, Contact

admin.site.register(Products)
admin.site.register(Contact)
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='ShopIndex'),
    path("about/", views.about, name='AboutUs'),
    path("contact/", views.contact, name='ContactUs'),
    path("productview/<int:id>", views.productview, name='ProductView'),
    path("tracker/", views.tracker, name='Tracker'),
    path("checkout/", views.checkout, name='CheckOut')

]
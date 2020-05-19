from django.shortcuts import render
from django.http import HttpResponse
from .models import Products,Contact
from math import ceil


# Create your views here.

def index(request):
    product = Products.objects.all()
    n = len(product)
    no_of_slides = n / 4 + ceil(n / 4 - n // 4)
    #allprods =[[product, range(1, int(no_of_slides)), no_of_slides], [product, range(1, int(no_of_slides)), no_of_slides]]
    allprods = []
    catprods = Products.objects.values('category', 'id')
    print(catprods)
    cats = {item['category'] for item in catprods}
    print(cats)
    for cat in cats:
        prod = Products.objects.filter(category= cat)
        n = len(prod)
        no_of_slides = n / 4 + ceil(n / 4 - n // 4)
        allprods.append([prod, range(1, int(no_of_slides)), no_of_slides])

    params = {'allprods': allprods}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('query', '')
        print(name, email, phone, desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()

    return render(request, 'shop/contact.html')


def tracker(request):
    return render(request, 'shop/tracker.html')


def productview(request, id):
    product = Products.objects.filter(id= id)
    print(product)
    return render(request, 'shop/productview.html', {'product' : product[0]})


def checkout(request):
    return render(request, 'shop/checkout.html')

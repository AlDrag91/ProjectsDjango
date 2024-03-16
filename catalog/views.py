from django.shortcuts import render

from catalog.models import Product


def index(request):
    latest_products = Product.objects.order_by('-created_at')[:5]
    for product in latest_products:
        print(f"Название товара: {product.product_name}")

    return render(request, 'catalog/home2.html')


def contacts(request):
    print(request.POST.get('name'))
    print(request.POST.get('phone'))
    print(request.POST.get('message'))

    return render(request, 'catalog/contacts.html')

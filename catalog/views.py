from django.shortcuts import render

from catalog.models import Product, Contact


def index(request):
    latest_products = Product.objects.order_by('-created_at')[:5]
    for product in latest_products:
        print(f"Название товара: {product.product_name}")
    context = {
        'title': 'Главная'
    }

    return render(request, 'catalog/home2.html', context)


def contacts(request):
    contact = Contact.objects.all()
    context = {
        'list_contact': contact,
        'title': 'Контакты'
    }

    return render(request, 'catalog/contacts.html', context)


def catalog_products(request):
    catalog = Product.objects.all()
    context = {
        'list_products': catalog,
        'title': 'Каталог продуктов'
    }
    return render(request, 'catalog/catalog_products.html', context)

from django.shortcuts import render

from catalog.models import Product, Contact


def index(request):
    catalog = Product.objects.all()
    context = {
        'catalog': catalog,
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


def product(request, pk):
    category_item = Product.objects.get(pk=pk)
    context = {
        'list_products': Product.objects.filter(pk=pk),
        'title': f'Выбранный продукт {category_item.product_name}'
    }
    return render(request, 'catalog/product.html', context)

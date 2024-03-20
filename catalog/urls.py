from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, contacts, catalog_products

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('home/', index, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('catalog_products/', catalog_products, name='catalog_products')
]

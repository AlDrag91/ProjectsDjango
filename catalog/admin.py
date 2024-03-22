from django.contrib import admin
from catalog.models import Category, Product, Contact


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category')
    list_filter = ('category',)
    search_fields = ('category', 'title')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'purchase_price', 'category')
    list_filter = ('category',)
    search_fields = ('product_name', 'title')
    actions = ['product_media']


admin.site.register(Contact)

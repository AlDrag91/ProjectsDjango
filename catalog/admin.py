from django.contrib import admin
from catalog.models import Category, Product, Contact, Blog, Version


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


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content')
    actions = ['blog_preview']


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'version_number', 'version_name', 'current_version')
    list_filter = ('product_name',)

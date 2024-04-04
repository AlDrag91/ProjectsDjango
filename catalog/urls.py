from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, ContactsListView, ProductListView, BlogCreateView, BlogListView, BlogDetailView, \
    BlogUpdateView, BlogDeleteView, ProductDetailView, ProductCreateView, ProductDeleteView, ProductUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),

    path('contacts/', ContactsListView.as_view(), name='contacts'),

    path('product/', ProductListView.as_view(), name='product'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
    path('product_update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product_delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),

    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog_detail/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog_create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog_update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog_delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete')

]

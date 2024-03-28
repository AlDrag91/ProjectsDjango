from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, ContactsListView, ProductListView, BlogCreateView, BlogListView, BlogDetailView, \
    BlogUpdateView, BlogDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', ContactsListView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductListView.as_view(), name='product'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog_detail/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog_create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog_update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog_delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete')

]

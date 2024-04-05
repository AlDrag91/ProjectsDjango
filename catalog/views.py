from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from icecream import ic

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Contact, Blog, Version


def index(request):
    catalog = Product.objects.all()
    context = {
        'catalog': catalog,
        'title': 'Главная'
    }

    return render(request, 'catalog/home.html', context)


class ContactsListView(ListView):
    model = Contact
    contact = Contact.objects.all()
    extra_context = {
        'list_contact': contact,
        'title': 'Контакты'
    }


class ProductListView(ListView):
    model = Product

    def get_context_data(self, *args, **kwargs):
        contex_data = super().get_context_data(**kwargs)
        products_items = Product.objects.all()
        for product_item in products_items:
            active_version = Version.objects.filter(product_name=product_item, current_version=True)
            if active_version:
                product_item.active_version = active_version.values_list('version_number', flat=True)[0]
        contex_data['product'] = products_items
        contex_data['title'] = f'Продукты'
        ic(product_item.active_version)
        ic(products_items)
        return contex_data


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, *args, **kwargs):
        contex_data = super().get_context_data(*args, **kwargs)
        product_item = Product.objects.get(pk=self.kwargs.get('pk'))
        contex_data['product'] = product_item,
        contex_data['title'] = f'Выбранный продукт {product_item.product_name}'
        return contex_data


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product')
    extra_context = {
        'button_name': 'Создать Продукт',
        'title': 'Добавить Продукт'
    }


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product')
    extra_context = {
        'button_name': 'Изменить Продукт',
        'title': 'Изменение Продукта'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product')
    extra_context = {
        'title': 'Удаление Продукт'
    }


class BlogListView(ListView):
    model = Blog

    def get_context_data(self, *args, **kwargs):
        contex_data = super().get_context_data(*args, **kwargs)
        blog_list = Blog.objects.filter(is_published=True)
        contex_data['blog'] = blog_list
        contex_data['title'] = 'Блоги'
        return contex_data


class BlogDetailView(DetailView):
    model = Blog

    def get_context_data(self, *args, **kwargs):
        contex_data = super().get_context_data(*args, **kwargs)

        blog_item = Blog.objects.get(pk=self.kwargs.get('pk'))
        contex_data['blog'] = blog_item,
        contex_data['title'] = f'Выбранный блог {blog_item.title}'
        return contex_data

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.views_count += 1
        if self.object.views_count == 100:
            print(f"100!!!! {self.object.title}")
            # send_email(self.object)
        self.object.save()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'content', 'preview', 'is_published']
    success_url = reverse_lazy('catalog:blog')
    extra_context = {
        'button_name': 'Создать блог',
        'title': 'Создать Блог'
    }

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save()
            title = form.cleaned_data.get('title')
            self.object.slug = slugify(title)
            self.object.save()
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'content', 'preview', 'is_published']
    extra_context = {
        'button_name': 'Изменить блог',
        'title': 'Изменить Блог '
    }

    def get_success_url(self):
        return reverse_lazy('catalog:blog_detail', args=(self.kwargs['pk'],))


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog')
    extra_context = {
        'title': 'Удаление Блога '
    }

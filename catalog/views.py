from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from catalog.models import Product, Contact, Blog


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

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(pk=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        contex_data = super().get_context_data(*args, **kwargs)

        category_item = Product.objects.get(pk=self.kwargs.get('pk'))
        contex_data['list_products'] = category_item,
        contex_data['title'] = f'Выбранный продукт {category_item.product_name}'
        print(category_item)
        return contex_data


class BlogListView(ListView):
    model = Blog

    # blog_list = Blog.objects.filter(is_published=True)
    # extra_context = {
    #     'blog': blog_list,
    #     'title': 'Блоги'
    # }
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

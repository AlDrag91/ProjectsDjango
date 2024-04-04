from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    category = models.CharField(max_length=100, verbose_name='Категория')
    title = models.CharField(max_length=100, verbose_name='Описание ')

    def __str__(self):
        return f'{self.category}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Название продукта')
    title = models.CharField(max_length=150, verbose_name='Описание продукта')
    image_preview = models.ImageField(upload_to='product/', verbose_name='Изображение товара', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    purchase_price = models.IntegerField(verbose_name='Стоимость')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.product_name}, {self.category}, {self.title},{self.purchase_price}, {self.created_at}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    message = models.TextField()

    def __str__(self):
        return f'{self.name}, {self.phone}, {self.message}'


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=100)
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='blog_preview/', verbose_name='Изображение', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False, verbose_name='Публикация')
    views_count = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title}, {self.content}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'


class Version(models.Model):
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE, max_length=100)
    version_number = models.IntegerField(verbose_name='Номер версии')
    version_name = models.CharField(max_length=100, verbose_name='Название версии')
    current_version = models.BooleanField(default=True, verbose_name='Признак текущей версии')

    def __str__(self):
        return f'{self.version_number}, {self.version_name}, {self.product_name}, {self.current_version}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'

from django.core.management import BaseCommand
from catalog.models import Category, Product
import json


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('data_catalog.json', 'r') as file:
            data_catalog = json.load(file)
        return data_catalog
        # Здесь мы получаем данные из фикстурв с категориями

    @staticmethod
    def json_read_products():
        with open('data_product.json', 'r') as file:
            data_product = json.load(file)
        return data_product
        # Здесь мы получаем данные из фикстурв с продуктами

    def handle(self, *args, **options):

        Product.objects.all().delete()
        Category.objects.all().delete()

        # Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(**category)
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)
        print(category_for_create)

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_for_create.append(
                Product(**product)
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)
        print(product_for_create)

from django.core.management import BaseCommand
from catalog.models import Category, Product
import json


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('data_catalog.json', 'r', encoding='utf-8') as file:
            data_catalog = json.load(file)
        with open('data_product.json', 'r', encoding='utf-8') as file:
            data_product = json.load(file)

        Product.objects.all().delete()
        Category.objects.all().delete()

        # Создайте списки для хранения объектов
        category_for_create = []
        product_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in data_catalog:
            category_for_create.append(
                Category(pk=category["pk"], category=category["fields"]["category"], title=category["fields"]["title"])
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)
        print(f'Команда на добавление категорий прошла\n {category_for_create}')

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in data_product:
            category_instance = Category.objects.get(id=product["fields"]["category"])
            product_for_create.append(
                Product(pk=product["pk"], product_name=product["fields"]["product_name"],
                        title=product["fields"]["title"], image_preview=product["fields"]["image_preview"],
                        category=category_instance, purchase_price=product["fields"]["purchase_price"],
                        created_at=product["fields"]["created_at"], updated_at=product["fields"]["updated_at"])
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)
        print(f'Команда на добавление продуктов прошла\n {product_for_create}')

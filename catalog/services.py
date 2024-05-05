from catalog.models import Category
from config.settings import CACHES_ENABLED
from django.core.cache import cache


def get_category_from_cache():
    """Получение данных категорий из кеша или запись их в кеш"""
    if not CACHES_ENABLED:
        return Category.objects.all()
    key = 'category_list'
    category = cache.get(key)
    if category is not None:
        return category
    category = Category.objects.all()
    cache.set(key, category)
    return category

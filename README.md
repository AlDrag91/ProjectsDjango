Django:
Начало работы:
1. Создание проекта Django 
2. Создание приложение catalog
3. Внесены настройки проекта и сделаны настройку URL
4. Два шаблона home и contacts
5. Реализованно 2 контейнера

Работа с ORM:
1. Подключена БД postgresql и внесена настройка в settings
2. Созданы модели с полями и описаны настройки 
3. Перемещено отображение моделей в базу данных с помощью инструмента миграций
4. Добавлены настройки в admin.py 
5. Добавлен список категорий(shell):
        - python manage.py shell
        - from catalog.models import Category
        - Category.objects.create(category='Продукты', title='Продукты питания,напитки')
        - Category.objects.create(category='Электроника', title='Техника для дома, портативная электроника')
        - Category.objects.create(category='Авто', title='Запчасть и товары  для автомобилей')
        - Category.objects.all() 
        - Category.objects.get(pk=2)__dict__
        - Category.objects.filter(category = 'Авто')
        - Category.objects.exclude(category = 'Авто')
6. Созданы фикстуры: python -Xutf8 manage.py dumpdata catalog -o db.json
                     python -Xutf8 manage.py dumpdata catalog.Category -o data_catalog.json
                     python -Xutf8 manage.py dumpdata catalog.Product -o data_product.json
7. Написана кастомная команда заполнение Category и Product
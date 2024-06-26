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

Шаблонизация 
В режиме разработки использую такую настройку STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATIC_ROOT = os.path.join(BASE_DIR, '/static/')

1. Создан контроллер и шаблон catalog_products 
2. Создан шаблон страницы с карточками товаров все данные обрезано до 50 знаков
3. Создан шаблон выбор 1 товара описание обрезано до 100 знаков
4. Выделен базовый шаблон, выделен под шаблон 
5. Реализован шаблонный фильтр для доступа к медиафайлам

FBV и CBV:

1. Переведены имеющиеся контроллеры с FBV на CBV.
2. Создана модель блоговой записи.
    Для редактирования или удаления надо выбрать блог.
3. - Реализован счетчик просмотров.
   - Фильтрация блогов которые опубликованные
   - Динамически формируется slug name
   - После редактирования успешного перенаправляет пользователя на просмотр этой статьи.
4. Добавлен в метод get класса BlogDetailView проверка кол-во просмотров.

Формы:
1. Реализованно для модели Продукты механизм CRUD и задействован django.forms.
2. Реализованна валидация для создания продуктов. 
В названии и описании запрещены слова:казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар.
3. Добавлена Модель - Версия (добавление версии в изменение продукта)
4. Добавлена реализация работы с формами

Аутентификация:
Подготовка:
- Изменено версия Django==4.2,
- Создание приложения users,
- Откатил миграцию, удалил миграцию, создал миграцию и применил ее
1. Реализовано авторизация пользователя на сайте с помощью почты и пароля,
2. Реализовано регистрацию пользователя (и изменение данных пользователя в профиле),
3. Добавлено поле в Моделях продуктов Публициста (Создавать продукт может только зарегистрированный пользователь)
4. Добавлена Верификация по почте при регистрации
5. При создании продукта добавлено поле кто опубликовал
6. Реализовано восстановление пароля по mail
7. Закрыто для не авторизованных пользователей добавление и изменение продуктов

Права доступа:
1. Для не зарегистрированного пользователя при изменении данных отправляет на страницу авторизации
2. Добавлены права доступа - 'отменять публикацию продукта', 'менять описание любого продукта', 'менять категорию любого продукта'.

Кеширование и работа с переменными окружения:
1. Установлен брокер Redis
2. Внесены настройки для кеширования
3. В catalog/urls.py Кешируем контролер ProductDetailView
4. Добавлено низкоуровневое кеширование для списка категорий.
5. Вынесены необходимые настройки в переменные окружения

# Generated by Django 4.2 on 2024-05-01 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_product_publisher'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Публикация'),
        ),
    ]

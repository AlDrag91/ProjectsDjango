# Generated by Django 5.0.3 on 2024-03-22 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_product_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Описание продукта'),
        ),
    ]
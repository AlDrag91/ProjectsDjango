# Generated by Django 5.0.3 on 2024-03-14 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='manufactured_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

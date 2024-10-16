# Generated by Django 5.1.1 on 2024-10-12 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("robot", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pickuppoint",
            name="marketplace",
            field=models.CharField(
                choices=[
                    ("ozon", "Озон"),
                    ("wb", "ВБ"),
                    ("yandex", "Яндекс Маркет"),
                    ("cdek", "СДЭК"),
                ],
                max_length=50,
                verbose_name="Название маркетплейса",
            ),
        ),
    ]

# Generated by Django 4.1.4 on 2023-01-02 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0003_product_public"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="public",
            field=models.BooleanField(default=True),
        ),
    ]

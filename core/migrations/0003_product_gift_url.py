# Generated by Django 3.2.7 on 2023-06-22 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_product_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='gift_url',
            field=models.CharField(blank=True, default=' ', max_length=1000, null=True),
        ),
    ]

# Generated by Django 4.0.4 on 2022-04-25 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20220415_2229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collection',
            old_name='feautured_product',
            new_name='featured_product',
        ),
    ]

# Generated by Django 4.1.6 on 2023-02-16 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_store'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='products',
        ),
        migrations.DeleteModel(
            name='Store',
        ),
    ]

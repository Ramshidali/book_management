# Generated by Django 3.2.10 on 2024-02-17 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20240217_0734'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
    ]
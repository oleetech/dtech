# Generated by Django 4.2.8 on 2023-12-18 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Purchasing', '0003_purchaseitem_quatationno_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaseitem',
            name='quatationNo',
        ),
        migrations.RemoveField(
            model_name='purchaseorderinfo',
            name='quatationNo',
        ),
    ]
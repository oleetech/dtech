# Generated by Django 4.2.8 on 2023-12-18 20:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('BusinessPartner', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Sales', '0002_deliveryinfo_deliveryitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='ARInvoiceInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('O', 'Open'), ('H', 'Hold'), ('C', 'Close'), ('F', 'Canceled')], default='O', max_length=1)),
                ('docNo', models.PositiveIntegerField(default=1, unique=True)),
                ('address', models.CharField(blank=True, max_length=250)),
                ('created', models.DateField(default=django.utils.timezone.now)),
                ('totalAmount', models.DecimalField(blank=True, decimal_places=4, default=0, max_digits=10, null=True)),
                ('totalQty', models.DecimalField(blank=True, decimal_places=4, default=0, max_digits=10, null=True)),
                ('salesOrder', models.PositiveIntegerField(default=0)),
                ('deliveryNo', models.PositiveIntegerField(default=0, unique=True)),
                ('customerName', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='BusinessPartner.businesspartner')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('sales_employee', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Sales.salesemployee')),
            ],
            options={
                'verbose_name': 'AR Invoice',
                'verbose_name_plural': 'AR Invoice',
            },
        ),
        migrations.CreateModel(
            name='ARInvoiceItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(default=django.utils.timezone.now)),
                ('code', models.CharField(default='', max_length=20, null=True)),
                ('name', models.CharField(default='', max_length=100, null=True)),
                ('uom', models.CharField(default='', max_length=20, null=True)),
                ('quantity', models.DecimalField(decimal_places=4, default=0, max_digits=10)),
                ('size', models.CharField(default='', max_length=100, null=True)),
                ('color', models.CharField(default='', max_length=100, null=True)),
                ('style', models.CharField(default='', max_length=100, null=True)),
                ('gweight', models.CharField(default='', max_length=100, null=True)),
                ('nweight', models.CharField(default='', max_length=100, null=True)),
                ('ctnno', models.CharField(default='', max_length=100, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=4, default=0, max_digits=10, null=True)),
                ('priceTotal', models.DecimalField(blank=True, decimal_places=4, default=0, max_digits=10, null=True)),
                ('deliveryNo', models.PositiveIntegerField(default=0)),
                ('deliverylineNo', models.PositiveIntegerField(default=0)),
                ('lineNo', models.PositiveIntegerField(default=0)),
                ('orderNo', models.PositiveIntegerField(default=0)),
                ('order', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Sales.arinvoiceinfo')),
            ],
        ),
    ]

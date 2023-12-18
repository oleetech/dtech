# Generated by Django 4.2.8 on 2023-12-18 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Sales', '0005_remove_contractorworker_contractor_and_more'),
        ('ProjectManagement', '0004_projectbill_amount_projectbill_bill_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkFlow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('perday_complete', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sales_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sales.salesorderinfo')),
            ],
        ),
    ]
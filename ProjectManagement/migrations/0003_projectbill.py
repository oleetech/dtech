# Generated by Django 4.2.8 on 2023-12-18 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Sales', '0005_remove_contractorworker_contractor_and_more'),
        ('ProjectManagement', '0002_contractorworker_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='project_bills/')),
                ('contractor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProjectManagement.contractor')),
                ('sales_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sales.salesorderinfo')),
            ],
        ),
    ]

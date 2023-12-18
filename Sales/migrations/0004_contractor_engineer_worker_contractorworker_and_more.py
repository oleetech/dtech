# Generated by Django 4.2.8 on 2023-12-18 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Sales', '0003_arinvoiceinfo_arinvoiceitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Engineer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ContractorWorker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contractor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sales.contractor')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sales.worker')),
            ],
        ),
        migrations.CreateModel(
            name='AsignEngCon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contractors', models.ManyToManyField(to='Sales.contractor')),
                ('engineers', models.ManyToManyField(to='Sales.engineer')),
                ('sales_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sales.salesorderinfo')),
            ],
        ),
    ]
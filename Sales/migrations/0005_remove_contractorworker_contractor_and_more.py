# Generated by Django 4.2.8 on 2023-12-18 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sales', '0004_contractor_engineer_worker_contractorworker_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contractorworker',
            name='contractor',
        ),
        migrations.RemoveField(
            model_name='contractorworker',
            name='worker',
        ),
        migrations.DeleteModel(
            name='AsignEngCon',
        ),
        migrations.DeleteModel(
            name='Contractor',
        ),
        migrations.DeleteModel(
            name='ContractorWorker',
        ),
        migrations.DeleteModel(
            name='Engineer',
        ),
        migrations.DeleteModel(
            name='Worker',
        ),
    ]

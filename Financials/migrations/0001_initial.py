# Generated by Django 4.2.8 on 2023-12-16 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChartOfAccounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(max_length=10, unique=True)),
                ('account_name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('opening_balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('is_active', models.BooleanField(default=True)),
                ('account_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Financials.accounttype')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=4, max_digits=15)),
                ('transaction_type', models.CharField(choices=[('debit', 'Debit'), ('credit', 'Credit')], max_length=10)),
                ('date', models.DateField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Financials.chartofaccounts')),
            ],
        ),
        migrations.CreateModel(
            name='JournalEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=4, max_digits=15)),
                ('date', models.DateField()),
                ('bill_image', models.ImageField(blank=True, null=True, upload_to='journal_entry_bills/')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Financials.chartofaccounts')),
            ],
        ),
    ]

from django.db import models

class AccountType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name


class ChartOfAccounts(models.Model):
    account_number = models.CharField(max_length=10, unique=True)
    account_name = models.CharField(max_length=100)
    account_type = models.ForeignKey(AccountType, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    opening_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.account_number} - {self.account_name}"
    
    
class JournalEntry(models.Model):
    account = models.ForeignKey(ChartOfAccounts, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=4)
    date = models.DateField()
    bill_image = models.ImageField(upload_to='journal_entry_bills/', null=True, blank=True)

    def __str__(self):
        return f"{self.date} - {self.account} - {self.amount}"   
    

class Transaction(models.Model):
    account = models.ForeignKey(ChartOfAccounts, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=4)
    transaction_type = models.CharField(max_length=10, choices=[('debit', 'Debit'), ('credit', 'Credit')])
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.date} - {self.account} - {self.transaction_type} - {self.amount}"    
    

from Sales.models import SalesOrderInfo
from django.utils import timezone
class ProjectIncomeSummary(models.Model):
    sales_order = models.OneToOneField(SalesOrderInfo, on_delete=models.CASCADE, related_name='project_income_summary')
    project_name = models.CharField(max_length=255)
    project_description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    total_cost = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    total_received = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    class Meta:
        verbose_name = 'Project Income Summary'
        verbose_name_plural = 'Project Income Summaries'

    def __str__(self):
        return f"Project Income Summary - {self.project_name}"

class ReceivedAmount(models.Model):
    project_income_summary = models.ForeignKey(ProjectIncomeSummary, on_delete=models.CASCADE, related_name='received_amounts')
    amount = models.DecimalField(max_digits=10, decimal_places=4)
    received_date = models.DateField(default=timezone.now)
    image = models.ImageField(upload_to='received_amount_images/', blank=True, null=True)

    def __str__(self):
        return f"Received Amount - {self.amount}"

class Cost(models.Model):
    project_income_summary = models.ForeignKey(ProjectIncomeSummary, on_delete=models.CASCADE, related_name='costs')
    description = models.CharField(max_length=250)
    amount = models.DecimalField(max_digits=10, decimal_places=4)
    image = models.ImageField(upload_to='cost_images/', blank=True, null=True)

    def __str__(self):
        return f"Cost - {self.amount} ({self.description})"     
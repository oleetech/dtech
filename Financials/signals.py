from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from Financials.models import ChartOfAccounts, Transaction,JournalEntry


@receiver(post_save, sender=JournalEntry)
def create_journal_transactions(sender, instance, **kwargs):
    pass
# Connect the signal handler to the DeliveryInfo model
post_save.connect(create_journal_transactions, sender=JournalEntry)
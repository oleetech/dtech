from django.db import models

from GeneralSettings.models import Unit
from datetime import date
from django.contrib.auth.models import User

class ItemGroup(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name
    
class Item(models.Model):
    code = models.CharField(max_length=20,default='',null=True)
    name = models.CharField(max_length=100,default='',null=True)
    description = models.TextField(default='',blank=True)
    unit = models.ForeignKey(Unit, on_delete=models.SET_DEFAULT, default=1)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    item_group = models.ForeignKey(ItemGroup, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=4,default=0)

    class Meta:
    # Add any other fields you need
        verbose_name = 'Item Master Data'
        verbose_name_plural = 'Item Master Data'    
    def __str__(self):
        return self.name

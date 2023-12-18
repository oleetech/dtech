
from django.db import models
from ItemMasterData.models import Item
from GeneralSettings.models import Unit,Department
from django.contrib.auth.models import User
from django.db.models import Sum
from Sales.models import SalesOrderItem
from django.utils import timezone
'''
  ____    _   _   _      ___     __     __  __           _                   _           _       
 | __ )  (_) | | | |    / _ \   / _|   |  \/  |   __ _  | |_    ___   _ __  (_)   __ _  | |  ___ 
 |  _ \  | | | | | |   | | | | | |_    | |\/| |  / _` | | __|  / _ \ | '__| | |  / _` | | | / __|
 | |_) | | | | | | |   | |_| | |  _|   | |  | | | (_| | | |_  |  __/ | |    | | | (_| | | | \__ \
 |____/  |_| |_| |_|    \___/  |_|     |_|  |_|  \__,_|  \__|  \___| |_|    |_|  \__,_| |_| |___/
                                                                                                 

'''
# Create your models here.
class BillOfMaterials(models.Model):
    code = models.CharField(max_length=20,default='',null=True)
    name = models.CharField(max_length=100,default='',null=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=4)
    uom = models.CharField(max_length=20,default='',null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.id}"
class ChildComponent(models.Model):
    bill_of_materials = models.ForeignKey(BillOfMaterials, on_delete=models.CASCADE, related_name='child_components')
    code = models.CharField(max_length=20,default='',null=True)
    name = models.CharField(max_length=100,default='',null=True)
    uom = models.CharField(max_length=20,default='',null=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=4)

    
    
'''
  ____                       _                  _     _                      ___               _               
 |  _ \   _ __    ___     __| |  _   _    ___  | |_  (_)   ___    _ __      / _ \   _ __    __| |   ___   _ __ 
 | |_) | | '__|  / _ \   / _` | | | | |  / __| | __| | |  / _ \  | '_ \    | | | | | '__|  / _` |  / _ \ | '__|
 |  __/  | |    | (_) | | (_| | | |_| | | (__  | |_  | | | (_) | | | | |   | |_| | | |    | (_| | |  __/ | |   
 |_|     |_|     \___/   \__,_|  \__,_|  \___|  \__| |_|  \___/  |_| |_|    \___/  |_|     \__,_|  \___| |_|   
                                                                                                               
'''


from Sales.models import SalesOrderInfo,SalesOrderItem
class Production(models.Model):
    Status_CHOICES = [
        ('P', 'Planned'),
        ('R', 'Released'),
        ('C', 'Close'),
        ('F', 'Canceled')
        
    ]
    status = models.CharField(max_length=1, choices=Status_CHOICES,default='P')
    code = models.CharField(max_length=20,default='',null=True)
    name = models.CharField(max_length=100,default='',null=True)
    uom =  models.CharField(max_length=100,default='',null=True)    
    quantity = models.DecimalField(max_digits=10, decimal_places=4)
    salesOrder = models.PositiveIntegerField(default=1)
    created = models.DateField(default=timezone.now, editable=True)
    order_date = models.DateField(default=timezone.now)
    start_date = models.DateField(default=timezone.now)
    due_date = models.DateField(default=timezone.now)
    docno = models.PositiveIntegerField(unique=True,default=1)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    remarks = models.CharField(max_length=250,default='',blank=True)
  
    class Meta:

        verbose_name = ' Production Order'
        verbose_name_plural = 'Production Order'    
        
    def __str__(self):
        return f"{self.docno}"

class ProductionComponent(models.Model):
    production = models.ForeignKey(Production, on_delete=models.CASCADE, related_name='production_components')
    docNo = models.PositiveIntegerField(default=1, unique=False)  
    lineNo = models.CharField(max_length=4,default='0') # Add the lineNo field    
    code = models.CharField(max_length=20,default='',null=True)
    salesOrder= models.PositiveIntegerField(default=1)
    name = models.CharField(max_length=100,default='',null=True)
    uom =  models.CharField(max_length=100,default='',null=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=4)
    created = models.DateField(default=timezone.now, editable=True)
    
    def save(self, *args, **kwargs):
        if self.salesOrder:
            

            self.created = self.production.created
        if self.docNo:
            self.docNo = self.production.docno                          
        super().save(*args, **kwargs)   
    # def __str__(self):
    #     return self.name   
    

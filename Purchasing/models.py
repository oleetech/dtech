from django.db import models

from django.db import models
from django.utils import timezone
from BusinessPartner.models import BusinessPartner 
from ItemMasterData.models import Item
from django.contrib.auth.models import User

class PurchaseQuotetionInfo(models.Model):
    Status_CHOICES = [
        ('O', 'Open'),
        ('H', 'Hold'),
        ('C', 'Close'),
        ('F', 'Canceled')
        
    ] 
    status = models.CharField(max_length=1, choices=Status_CHOICES,default='O')      
    docNo = models.PositiveIntegerField(default=1, unique=True)
    customerName = models.ForeignKey(BusinessPartner, on_delete=models.CASCADE, null=True, default=None)
    address = models.CharField(max_length=250,blank=True)
    created = models.DateField(default=timezone.now)
    totalAmount = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True,default=0)
    totalQty = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:

        verbose_name = 'Purchase Quotetion'
        verbose_name_plural = 'Purchase Quotetion'
        
    def __str__(self):
        return f"{self.docNo}"   
    

class PurchaseQuotetionItem(models.Model):
    created = models.DateField(default=timezone.now, editable=True)
    order = models.ForeignKey(PurchaseQuotetionInfo, on_delete=models.CASCADE, null=True, default=None)    
    code = models.CharField(max_length=20,default='',null=True)
    name = models.CharField(max_length=100,default='',null=True)    
    uom = models.CharField(max_length=20,default='',null=True)  
    quantity = models.DecimalField(max_digits=15, decimal_places=4,default=0)
    price = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True, default=0)
    priceTotal = models.DecimalField(max_digits=15, decimal_places=4,null=True, blank=True, default=0)
    docNo = models.PositiveIntegerField(default=1, unique=False)      
    lineNo = models.PositiveIntegerField(default=0)  # Add the lineNo field
    

    def save(self, *args, **kwargs):
        if self.created:


            self.created = self.order.created
                   
        super().save(*args, **kwargs)       
    def __str__(self):
        return f": {self.docNo}"



class PurchaseOrderInfo(models.Model):
    Status_CHOICES = [
        ('O', 'Open'),
        ('H', 'Hold'),
        ('C', 'Close'),
        ('F', 'Canceled')
    ] 
    status = models.CharField(max_length=1, choices=Status_CHOICES, default='O')  
    docNo = models.PositiveIntegerField(default=1, unique=True)
    customerName = models.ForeignKey(BusinessPartner, on_delete=models.CASCADE, null=True, default=None)
    address = models.CharField(max_length=250,blank=True)
    created = models.DateField(default=timezone.now)
    totalAmount = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True,default=0)
    totalQty = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:

        verbose_name = 'Purchase Order'
        verbose_name_plural = 'Purchase Order'
        
    def __str__(self):
        return f"{self.docNo}"

class PurchaseItem(models.Model):
    created = models.DateField(default=timezone.now, editable=True)    
    order = models.ForeignKey(PurchaseOrderInfo, on_delete=models.CASCADE, null=True, default=None)    
    code = models.CharField(max_length=20,default='',null=True)
    name = models.CharField(max_length=100,default='',null=True)    
    uom = models.CharField(max_length=20,default='',null=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=4,default=0)
    price = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True, default=0)
    priceTotal = models.DecimalField(max_digits=15, decimal_places=4,null=True, blank=True, default=0)
    lineNo = models.PositiveIntegerField(default=0)  # Add the lineNo field
    docNo = models.PositiveIntegerField(default=1, unique=False)      
    def save(self, *args, **kwargs):
        if self.created:            
            self.created = self.order.created
        if self.docNo:
            self.docNo = self.order.docNo                       
        super().save(*args, **kwargs)  
            
    def __str__(self):
        return f": {self.order}"
    
    
class ApInvoiceInfo(models.Model):
    docNo = models.PositiveIntegerField(default=1, unique=True)
    customerName = models.ForeignKey(BusinessPartner, on_delete=models.CASCADE, null=True, default=None)
    address = models.CharField(max_length=250,blank=True)
    created = models.DateField(default=timezone.now)
    totalAmount = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True,default=0)
    totalQty = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    goodsreReiptNo = models.PositiveIntegerField(default=0)
    class Meta:
        verbose_name = 'Ap Invoice'
        verbose_name_plural = 'Ap Invoice'
        
    def __str__(self):
        return f"{self.docNo}"   
    
class ApInvoiceItem(models.Model):
    created = models.DateField(default=timezone.now, editable=True)                
    order = models.ForeignKey(ApInvoiceInfo, on_delete=models.CASCADE, null=True, default=None)    
    code = models.CharField(max_length=20,default='',null=True)
    name = models.CharField(max_length=100,default='',null=True)    
    uom = models.CharField(max_length=20,default='',null=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=4,default=0)
    price = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True, default=0)
    priceTotal = models.DecimalField(max_digits=15, decimal_places=4,null=True, blank=True, default=0)
    docNo = models.PositiveIntegerField(default=1, unique=False)        
    goodsreReiptNo = models.PositiveIntegerField(default=0)
    lineNo =  models.PositiveIntegerField(default=0)     
    def save(self, *args, **kwargs):
        if self.created:            
            self.created = self.order.created
        if self.docNo:
            self.docNo = self.order.docNo                       
        super().save(*args, **kwargs)       
    def __str__(self):
        return f": {self.order}"         
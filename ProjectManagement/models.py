from django.db import models
from Sales.models import SalesOrderInfo
class Engineer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Worker(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Contractor(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class ContractorWorker(models.Model):
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True, default=None)

    def __str__(self):
        return f"{self.contractor} - {self.worker}"    

class AsignEngCon(models.Model):
    sales_order = models.ForeignKey(SalesOrderInfo, on_delete=models.CASCADE)
    engineers = models.ManyToManyField(Engineer)
    contractors = models.ManyToManyField(Contractor)

    def __str__(self):
        return f"{self.sales_order} - Engineers: {', '.join(str(engineer) for engineer in self.engineers.all())}, Contractors: {', '.join(str(contractor) for contractor in self.contractors.all())}"  
    
    
class ProjectBill(models.Model):
    TYPE_CHOICES = [
        ('LABOUR', 'Labour Bill'),
        ('MATERIALS', 'Materials'),
         ('OTHERS', 'OTHERS'),
    ]
    sales_order = models.ForeignKey(SalesOrderInfo, on_delete=models.CASCADE)
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2,default =0)
    bill_type = models.CharField(max_length=10, choices=TYPE_CHOICES,default="LABOUR")
    image = models.ImageField(upload_to='project_bills/', blank=True, null=True)
    # Add other fields related to the project bill

    def __str__(self):
        return f"Project Bill - {self.sales_order}" 
    
    
class WorkFlow(models.Model):
    sales_order = models.ForeignKey(SalesOrderInfo, on_delete=models.CASCADE)
    work_amount = models.DecimalField(max_digits=10, decimal_places=2)
    perday_complete = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f"WorkFlow - {self.sales_order}"       


from django.contrib.auth.models import User
class DailyTaskProject(models.Model):
    work_flow = models.ForeignKey(WorkFlow, on_delete=models.CASCADE)
    date = models.DateField()
    work_amount_submitted = models.DecimalField(max_digits=10, decimal_places=2)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Daily Task - {self.date} - {self.work_flow}"
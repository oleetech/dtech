from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

'''
  ____                 _                           _     _                 
 |  _ \    ___   ___  (_)   __ _   _ __     __ _  | |_  (_)   ___    _ __  
 | | | |  / _ \ / __| | |  / _` | | '_ \   / _` | | __| | |  / _ \  | '_ \ 
 | |_| | |  __/ \__ \ | | | (_| | | | | | | (_| | | |_  | | | (_) | | | | |
 |____/   \___| |___/ |_|  \__, | |_| |_|  \__,_|  \__| |_|  \___/  |_| |_|
                           |___/                                           

'''

class Designation(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    
    
'''
  ____                                  _                                _   
 |  _ \    ___   _ __     __ _   _ __  | |_   _ __ ___     ___   _ __   | |_ 
 | | | |  / _ \ | '_ \   / _` | | '__| | __| | '_ ` _ \   / _ \ | '_ \  | __|
 | |_| | |  __/ | |_) | | (_| | | |    | |_  | | | | | | |  __/ | | | | | |_ 
 |____/   \___| | .__/   \__,_| |_|     \__| |_| |_| |_|  \___| |_| |_|  \__|
                |_|                                                          
'''     
class Department(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name





'''___                       _                               
 | ____|  _ __ ___    _ __   | |   ___    _   _    ___    ___ 
 |  _|   | '_ ` _ \  | '_ \  | |  / _ \  | | | |  / _ \  / _ \
 | |___  | | | | | | | |_) | | | | (_) | | |_| | |  __/ |  __/
 |_____| |_| |_| |_| | .__/  |_|  \___/   \__, |  \___|  \___|
                     |_|                  |___/               
'''    
class Employee(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    RELIGION_CHOICES = [
        ('Christianity', 'Christianity'),
        ('Islam', 'Islam'),
        ('Hinduism', 'Hinduism'),
        ('Buddhism', 'Buddhism'),
        ('Sikhism', 'Sikhism'),
        ('Judaism', 'Judaism'),
        ('Other', 'Other'),
    ]

    MARITAL_STATUS_CHOICES = [
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed'),
    ]



    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    fatherName = models.CharField(max_length=100, blank=True, null=True)
    motherName = models.CharField(max_length=100, blank=True, null=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,blank=True, null=True)
    
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,blank=True, null=True,default='M')
    birth_date = models.DateField(blank=True, null=True)
    hire_date = models.DateField(blank=True, null=True)
    designation = models.CharField(max_length=100,blank=True, null=True)
    id_no = models.PositiveIntegerField(default=1, unique=True,blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2,default=1,blank=True, null=True)
    joiningSalary = models.DecimalField(max_digits=10, decimal_places=2,default=1)
    nid = models.CharField(max_length=30, blank=True, null=True)
    
    email = models.EmailField(unique=True,blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    active = models.BooleanField(default=False)  # New field for active status
    bloodGroup = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES,blank=True, null=True)
    religion = models.CharField(max_length=20, choices=RELIGION_CHOICES,blank=True, null=True)
    # Define the marital_status field with choices
    maritalStatus = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES,blank=True, null=True)
    localAddress = models.CharField(max_length=200,blank=True, null=True)
    permanentAddress = models.CharField(max_length=200,blank=True, null=True)   
    photo = models.ImageField(upload_to='employee_photos/',null=True, blank=True)     
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        verbose_name = 'Employee Master Data'
        verbose_name_plural = 'Employee Master Data'
            
    def __str__(self):
        return f"{self.id_no}"  
    
    
    
class NomineeInformation(models.Model):


    RELATIONSHIP_CHOICES = (
        ('Spouse', 'Spouse'),
        ('Child', 'Child'),
        ('Parent', 'Parent'),
        ('Sibling', 'Sibling'),
        ('Other', 'Other'),
    )

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    nid = models.CharField(max_length=30, blank=True, null=True)
    relationship = models.CharField(max_length=10, choices=RELATIONSHIP_CHOICES)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    def __str__(self):
        return f"{self.employee.id_no}"     
        
'''
  _____                       _                                 ____                                                      _   
 | ____|  _ __ ___    _ __   | |   ___    _   _    ___    ___  |  _ \    ___     ___   _   _   _ __ ___     ___   _ __   | |_ 
 |  _|   | '_ ` _ \  | '_ \  | |  / _ \  | | | |  / _ \  / _ \ | | | |  / _ \   / __| | | | | | '_ ` _ \   / _ \ | '_ \  | __|
 | |___  | | | | | | | |_) | | | | (_) | | |_| | |  __/ |  __/ | |_| | | (_) | | (__  | |_| | | | | | | | |  __/ | | | | | |_ 
 |_____| |_| |_| |_| | .__/  |_|  \___/   \__, |  \___|  \___| |____/   \___/   \___|  \__,_| |_| |_| |_|  \___| |_| |_|  \__|
                     |_|                  |___/                                                                               

'''
class EmployeeDocument(models.Model):
    EMPLOYEE_DOCUMENT_TYPES = (
        ('Resume', 'Resume'),
        ('Contract', 'Contract'),
        ('ID Card', 'ID Card'),
        ('Other', 'Other'),
    )

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)  # Associate the document with an employee (User model in this case)
    document_name = models.CharField(max_length=100)
    document_type = models.CharField(max_length=20, choices=EMPLOYEE_DOCUMENT_TYPES)
    upload_date = models.DateTimeField(auto_now_add=True)
    document_file = models.FileField(upload_to='employee_documents/')

    def __str__(self):
        return self.document_name  

    
class EducationInformation(models.Model):
    # Existing fields
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)    
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=200)
    completion_year = models.PositiveIntegerField()  
    def __str__(self):
        return f'{self.employee.id_no}'      
class ExperienceInformation(models.Model):
    # Existing fields
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    education_info = models.ForeignKey(EducationInformation, on_delete=models.CASCADE, related_name='experiences')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)    
    def save(self, *args, **kwargs):
  
        if not self.employee :
            self.employee = self.education_info.employee  
            
        super().save(*args, **kwargs)  
        
class EmployeeBankInfo(models.Model):
    BANK_CHOICES = (
    ('Bank A', 'Bank A'),
    ('Bank B', 'Bank B'),
    ('Bank C', 'Bank C'),
    ('Bank D', 'Bank D'),
    # Add more banks as needed
)
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name='bank_info')
    account_number = models.CharField(max_length=20)
    bank_name = models.CharField(max_length=50, choices=BANK_CHOICES)     
    
    def __str__(self):
        return f" {self.employee.name}"   
    
    
'''
  _                                     ____                                        _   
 | |       ___    __ _  __   __   ___  |  _ \    ___    __ _   _   _    ___   ___  | |_ 
 | |      / _ \  / _` | \ \ / /  / _ \ | |_) |  / _ \  / _` | | | | |  / _ \ / __| | __|
 | |___  |  __/ | (_| |  \ V /  |  __/ |  _ <  |  __/ | (_| | | |_| | |  __/ \__ \ | |_ 
 |_____|  \___|  \__,_|   \_/    \___| |_| \_\  \___|  \__, |  \__,_|  \___| |___/  \__|
                                                          |_|                           
'''  
from datetime import datetime, timedelta
             
class LeaveRequest(models.Model):
    LEAVE_CHOICES = (
        ('casual_leave', 'Casual Leave'),
        ('medical_leave', 'Medical Leave'),
    )    
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    leave_type = models.CharField(max_length=20, choices=LEAVE_CHOICES, default='casual_leave')  # Set the default value
    leave_duration = models.DurationField(blank=True, null=True)
    
    reason = models.TextField()
    status = models.CharField(max_length=15, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')])  
    id_no = models.PositiveIntegerField(default=1, null=True,blank=True)
    def save(self, *args, **kwargs):
        # Set the id_no field to the employee's id_no
        if not self.id_no:
            self.id_no = self.employee.id_no
            
        # Calculate the leave duration
        if self.start_date and self.end_date:
            self.leave_duration = self.end_date - self.start_date + timedelta(days=1)            
            
            
        super().save(*args, **kwargs)       
    class Meta:
        unique_together = ('start_date', 'end_date','employee')      
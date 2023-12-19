from django.contrib import admin

from .models import Designation,Department,Employee,NomineeInformation,EmployeeDocument,EducationInformation,EducationInformation,ExperienceInformation,EmployeeBankInfo
from django import forms


class DesignationForm(forms.ModelForm):
    class Meta:
        model = Designation
        exclude = ['owner',]  # You can exclude fields if needed

        widgets = {
            # 'name': forms.TextInput(attrs={'readonly': 'readonly'}),
 
        }  



@admin.register(Designation)                             
class DesignationAdmin(admin.ModelAdmin):

    form = DesignationForm  
    change_form_template = 'admin/erp/change_form.html'   
    def save_model(self, request, obj, form, change):

        obj.owner = request.user if request.user.is_authenticated else None
          
        super().save_model(request, obj, form, change) 
        
    class Media: 
        js = ('bootstrap.bundle.min.js','js/dataTables.min.js')
        defer = True  # Add the defer attribute          
        css = {
            'all': ('css/bootstrap.min.css','css/admin_styles.css','css/dataTables.min.css'),
        }  

class EmployeeDocumentForm(forms.ModelForm):
    class Meta:
        model = EmployeeDocument  
        fields = '__all__'  # Use '__all__' to include all fields  
class EmployeeDocumentInline(admin.TabularInline):
    model = EmployeeDocument
    extra = 0  
    
    
# @admin.register(EmployeeDocument)
class EmployeeDocumentAdmin(admin.ModelAdmin):
    list_display = ('employee', 'document_name', 'document_type', 'upload_date')
    list_filter = ('document_type', 'upload_date')
    search_fields = ('employee__first_name', 'document_name')
    
           
class EducationInformationForm(forms.ModelForm):
    class Meta:
        model = EducationInformation
        fields = '__all__'  # You can specify the fields you want to include here

class EducationInformationInline(admin.TabularInline):
    model = EducationInformation
    extra = 0  # Set this to the desired number of empty forms to display    

# @admin.register(EducationInformation)           
class EducationInformationAdmin(admin.ModelAdmin):
    form = EducationInformationForm  # Use the custom form
    list_display = ['employee', 'degree', 'institution', 'completion_year']
    list_filter = ['employee', 'completion_year']
    search_fields = ['employee__username', 'degree', 'institution']
    list_per_page = 20

    class Media:

        css = {
            'all': ('css/bootstrap.min.css','css/admin_styles.css'),
        }     
  
    
           


class ExperienceInformationForm(forms.ModelForm):
    class Meta:
        model = ExperienceInformation
        fields = '__all__'  # You can specify the fields you want to include here    
class ExperienceInformationInline(admin.TabularInline):
    model = ExperienceInformation
    extra = 0            
class ExperienceInformationAdmin(admin.ModelAdmin):
    form = ExperienceInformationForm  # Use the custom form
    list_display = ['employee', 'position', 'company', 'start_date', 'end_date']
    list_filter = ['employee', 'start_date']
    search_fields = ['employee__username', 'position', 'company']
    list_per_page = 20           


class EmployeeBankInfoAdminForm(forms.ModelForm):
    class Meta:
        model = EmployeeBankInfo
        fields = '__all__'
        
class EmployeeBankInfoInline(admin.StackedInline):
    model = EmployeeBankInfo
    extra = 0
    
# @admin.register(EmployeeBankInfo)
class EmployeeBankInfoAdmin(admin.ModelAdmin):
    form = EmployeeBankInfoAdminForm
    list_display = ('employee', 'bank_name', 'account_number')
    # Add any other desired configurations for the admin model
    
class NomineeInformationForm(forms.ModelForm):
    class Meta:
        model = NomineeInformation
        fields = '__all__'
        
class NomineeInformationInline(admin.StackedInline):
    model = NomineeInformation
    extra = 0
            
# @admin.register(NomineeInformation)        
class NomineeInformationAdmin(admin.ModelAdmin):
    form = NomineeInformationForm
    
                
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ['owner',]  # You can exclude fields if needed

        widgets = {
            # 'name': forms.TextInput(attrs={'readonly': 'readonly'}),
 
        }  
@admin.register(Employee)                             
class EmployeeAdmin(admin.ModelAdmin):
  
    form = EmployeeForm  
    change_form_template = 'admin/erp/change_form.html' 
    inlines=[EducationInformationInline,ExperienceInformationInline,EmployeeDocumentInline,EmployeeBankInfoInline,NomineeInformationInline]    
    class Media: 
        js = ('js/bootstrap.bundle.min.js','js/dataTables.min.js')
        defer = True  # Add the defer attribute          
        css = {
            'all': ('css/bootstrap.min.css','css/admin_styles.css','css/dataTables.min.css'),
        }      
    def save_model(self, request, obj, form, change):

        obj.owner = request.user if request.user.is_authenticated else None

                      
        super().save_model(request, obj, form, change)   

from .models import LeaveRequest              
class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        exclude = ['id_no'] 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['employee'].widget = forms.Select(choices=Employee.objects.values_list('id', 'id_no'))

@admin.register(LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ('employee', 'start_date', 'end_date', 'reason', 'status')
    list_filter = ('status',)
    search_fields = ('employee__first_name', 'employee__last_name', 'start_date', 'end_date')
    form = LeaveRequestForm
    
from .models import Attendance    
@admin.register(Attendance)
class LeaveRequestAdmin(admin.ModelAdmin):  
        list_display = ('date','intime', 'outtime', 'status')  
        
        
        
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'time_slot_1', 'time_slot_2', 'time_slot_3', 'time_slot_4')
    search_fields = ('user__username', 'date')        
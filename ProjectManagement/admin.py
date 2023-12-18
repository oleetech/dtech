from django.contrib import admin

from .models import Engineer, Worker, Contractor, ContractorWorker, AsignEngCon

@admin.register(Engineer)
class EngineerAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name',)



class ContractorWorkerInline(admin.TabularInline):
    model = ContractorWorker
    extra = 0

@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    inlines = [ContractorWorkerInline]
    change_form_template = 'admin/erp/change_form.html'        
    
    


@admin.register(AsignEngCon)
class AsignEngConAdmin(admin.ModelAdmin):
    list_display = ('sales_order',)     



from .models import ProjectBill

@admin.register(ProjectBill)
class ProjectBillAdmin(admin.ModelAdmin):
    list_display = ('sales_order', 'contractor', 'amount', 'bill_type', 'image')


from .models import WorkFlow

@admin.register(WorkFlow)
class WorkFlowAdmin(admin.ModelAdmin):
    list_display = ('sales_order', 'work_amount', 'perday_complete')
    
    
from .models import DailyTaskProject
@admin.register(DailyTaskProject)
class DailyTaskProjectAdmin(admin.ModelAdmin):
    list_display = ('work_flow', 'date', 'work_amount_submitted','submitted_by')
    exclude= ['submitted_by']
    
    def save_model(self, request, obj, form, change):
        # Set the submitted_by field to the current user
        obj.submitted_by = request.user
        super().save_model(request, obj, form, change)    
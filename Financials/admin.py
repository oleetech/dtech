from django.contrib import admin

from .models import AccountType
admin.site.register(AccountType)


from .models import ChartOfAccounts
class ChartOfAccountsAdmin(admin.ModelAdmin):
    list_display = ('account_number', 'account_name', 'account_type', 'is_active')
    list_filter = ('account_type', 'is_active')
    search_fields = ('account_number', 'account_name')
    list_per_page = 20
admin.site.register(ChartOfAccounts, ChartOfAccountsAdmin)



from .models import JournalEntry
admin.site.register(JournalEntry)


from .models import Transaction
admin.site.register(Transaction)












from .models import ReceivedAmount, Cost, ProjectIncomeSummary

class ReceivedAmountInline(admin.TabularInline):
    model = ReceivedAmount
    extra = 0  # Set this to the desired number of empty forms to display    

class CostInline(admin.TabularInline):
    model = Cost
    extra = 0  # Set this to the desired number of empty forms to display    

class ProjectIncomeSummaryAdmin(admin.ModelAdmin):
    inlines = [ReceivedAmountInline, CostInline]
    list_display = ('project_name', 'created_at')
    search_fields = ('project_name',)

admin.site.register(ProjectIncomeSummary, ProjectIncomeSummaryAdmin)

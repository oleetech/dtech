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

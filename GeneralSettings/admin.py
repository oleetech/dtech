from django.contrib import admin


from .models import Company
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    # Define the fields to display and edit in the admin panel
    list_display = ('name', 'address')
    fields = ('name', 'logo','address','phone_number','email','website','established_year')
    # Disable the "Add" button in the admin panel
    def has_add_permission(self, request):
        return False


from .models import Currency
admin.site.register(Currency)


from .models import  Unit
admin.site.register(Unit)
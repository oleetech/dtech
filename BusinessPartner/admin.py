from django.contrib import admin
from django import forms


from .models import  BusinessPartner
class BusinessPartnerForm(forms.ModelForm):
    class Meta:
        model = BusinessPartner
        fields = ['code', 'vendor_type','name','address']  # সব ফিল্ড অবশ্যই যোগ করুন

    # যেহেতু BusinessPartner মডেলে currency_type এবং vendor_type ফিল্ডের একটি choices ফিল্ড আছে, আমি এটি একটি রেডিও বাটন রুপে দেখাতে চাই
    # currency_type = forms.ChoiceField(widget=forms.RadioSelect, choices=BusinessPartner.CURRENCY_TYPES)
    vendor_type = forms.ChoiceField(widget=forms.RadioSelect, choices=BusinessPartner.VENDOR_TYPES)

@admin.register(BusinessPartner)
class BusinessPartnerAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', 'code')
    list_filter = ( 'vendor_type',)
    ordering = ('name',)
    change_form_template = 'admin/erp/change_form.html'     
    form = BusinessPartnerForm 
    class Media:
        js = ('js/businesspartner.js',)
        defer = True
        css = {
            'all': ('css/bootstrap.min.css','css/admin_styles.css'),
        } 
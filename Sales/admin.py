from django.contrib import admin

'''
  ____            _                  _____                       _                               
 / ___|    __ _  | |   ___   ___    | ____|  _ __ ___    _ __   | |   ___    _   _    ___    ___ 
 \___ \   / _` | | |  / _ \ / __|   |  _|   | '_ ` _ \  | '_ \  | |  / _ \  | | | |  / _ \  / _ \
  ___) | | (_| | | | |  __/ \__ \   | |___  | | | | | | | |_) | | | | (_) | | |_| | |  __/ |  __/
 |____/   \__,_| |_|  \___| |___/   |_____| |_| |_| |_| | .__/  |_|  \___/   \__, |  \___|  \___|
                                                        |_|                  |___/               

'''  
from .models import SalesEmployee      
@admin.register(SalesEmployee)
class SalesEmployeeAdmin(admin.ModelAdmin): 
    list_display = ('first_name','last_name', 'email', 'phone_number', 'hire_date','active')
    search_fields = ('first_name', ) 
# Register your models here.



'''
  ____            _                   ___               _               
 / ___|    __ _  | |   ___   ___     / _ \   _ __    __| |   ___   _ __ 
 \___ \   / _` | | |  / _ \ / __|   | | | | | '__|  / _` |  / _ \ | '__|
  ___) | | (_| | | | |  __/ \__ \   | |_| | | |    | (_| | |  __/ | |   
 |____/   \__,_| |_|  \___| |___/    \___/  |_|     \__,_|  \___| |_|   
                                                                        
'''
from .models import SalesOrderInfo,SalesOrderItem
from django import forms
class SalesOrderItemForm(forms.ModelForm):
    class Meta:
        model = SalesOrderItem
        fields = ['code','name', 'uom','quantity','size','color','style','price','priceTotal','lineNo','description']
        widgets = {
            # 'ItemName': CustomModelSelect2Widget(model=Item, search_fields=['name__icontains'])
        }

class SalesOrderItemInline(admin.TabularInline):
    model = SalesOrderItem
    form = SalesOrderItemForm
    extra = 0

class SalesOrderInfoAdminForm(forms.ModelForm):
    class Meta:
        model = SalesOrderInfo
        fields = ['status','docNo','customerName', 'totalQty','sales_employee','totalAmount','remarks','edd']
        widgets = {
            'docNo': forms.TextInput(attrs={'readonly': 'readonly'}),
            'totalAmount': forms.TextInput(attrs={'readonly': 'readonly'}),
            'totalQty': forms.TextInput(attrs={'readonly': 'readonly'}),            
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not self.instance.pk:
            last_order = SalesOrderInfo.objects.order_by('-docNo').first()
            if last_order:
                next_order_number = last_order.docNo + 1
            else:
                next_order_number = 1

            self.initial['docNo'] = next_order_number
            
     
                    
@admin.register(SalesOrderInfo)
class SalesOrderInfoAdmin(admin.ModelAdmin):
    form = SalesOrderInfoAdminForm
    inlines = [SalesOrderItemInline]
    list_display = ('docNo','customerName', 'totalAmount', 'totalQty', 'created')
    search_fields = ('docNo', )    
    change_form_template = 'admin/erp/change_form.html'     
    

    
           
    class Media:
        js = ('js/salesorder.js',)
        defer = True
        css = {
            'all': ('css/bootstrap.min.css','css/admin_styles.css'),
        } 
    def save_model(self, request, obj, form, change):
        
        # Check if the main form is valid
        if not form.is_valid():
            self.message_user(request, "Main form is not valid.")
            return

        # Check if the inline formset data from request.POST is valid and not empty
        formset_data = request.POST.getlist('salesorderitem_set-TOTAL_FORMS')
        if not all(int(count) > 0 for count in formset_data):
            self.message_user(request, "SalesOrderItemInline is not valid or empty.")
            return
        
        if not obj.address:
            if obj.customerName :
                obj.address = obj.customerName.address
        obj.owner = request.user if request.user.is_authenticated else None                         
        super().save_model(request, obj, form, change)
        
 
'''
  ____           _   _                               
 |  _ \    ___  | | (_) __   __   ___   _ __   _   _ 
 | | | |  / _ \ | | | | \ \ / /  / _ \ | '__| | | | |
 | |_| | |  __/ | | | |  \ V /  |  __/ | |    | |_| |
 |____/   \___| |_| |_|   \_/    \___| |_|     \__, |
                                               |___/ 
'''        
from .models import DeliveryInfo, DeliveryItem

class DeliveryItemForm(forms.ModelForm):
    class Meta:
        model = DeliveryItem
        fields = ['code', 'name', 'uom', 'quantity', 'size', 'color', 'style', 'price', 'priceTotal', 'lineNo']

class DeliveryItemInline(admin.TabularInline):
    model = DeliveryItem
    form = DeliveryItemForm
    extra = 0

class DeliveryInfoAdminForm(forms.ModelForm):
    class Meta:
        model = DeliveryInfo
        fields = ['status', 'docNo', 'customerName', 'totalQty', 'sales_employee', 'totalAmount', 'delivertobuyerdate', 'challanreceiveddate']
        widgets = {
            'docNo': forms.TextInput(attrs={'readonly': 'readonly'}),
            'totalAmount': forms.TextInput(attrs={'readonly': 'readonly'}),
            'totalQty': forms.TextInput(attrs={'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not self.instance.pk:
            last_delivery = DeliveryInfo.objects.order_by('-docNo').first()
            if last_delivery:
                next_delivery_number = last_delivery.docNo + 1
            else:
                next_delivery_number = 1

            self.initial['docNo'] = next_delivery_number

@admin.register(DeliveryInfo)
class DeliveryInfoAdmin(admin.ModelAdmin):
    form = DeliveryInfoAdminForm
    inlines = [DeliveryItemInline]
    list_display = ('docNo', 'customerName', 'totalAmount', 'totalQty', 'created')
    search_fields = ('docNo', )
    change_form_template = 'admin/erp/change_form.html'

    class Media:
        js = ('js/delivery.js',)
        defer = True
        css = {
            'all': ('css/bootstrap.min.css', 'css/admin_styles.css'),
        }

    def save_model(self, request, obj, form, change):
        # Check if the main form is valid
        if not form.is_valid():
            self.message_user(request, "Main form is not valid.")
            return

        # Check if the inline formset data from request.POST is valid and not empty
        formset_data = request.POST.getlist('deliveryitem_set-TOTAL_FORMS')
        if not all(int(count) > 0 for count in formset_data):
            self.message_user(request, "DeliveryItemInline is not valid or empty.")
            return

        if not obj.address:
            if obj.customerName:
                obj.address = obj.customerName.address
        obj.owner = request.user if request.user.is_authenticated else None
        super().save_model(request, obj, form, change)        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
'''
     _      ____      ___                           _               
    / \    |  _ \    |_ _|  _ __   __   __   ___   (_)   ___    ___ 
   / _ \   | |_) |    | |  | '_ \  \ \ / /  / _ \  | |  / __|  / _ \
  / ___ \  |  _ <     | |  | | | |  \ V /  | (_) | | | | (__  |  __/
 /_/   \_\ |_| \_\   |___| |_| |_|   \_/    \___/  |_|  \___|  \___|
                                                                    

'''        
        
        
        
        
        
from .models import ARInvoiceInfo, ARInvoiceItem

class ARInvoiceItemForm(forms.ModelForm):
    class Meta:
        model = ARInvoiceItem
        fields = ['code','name', 'uom','quantity','price','priceTotal','deliveryNo','deliverylineNo','lineNo','orderNo']   

class ARInvoiceItemInline(admin.TabularInline):
    model = ARInvoiceItem
    form = ARInvoiceItemForm
    extra = 0

class ARInvoiceInfoAdminForm(forms.ModelForm):
    class Meta:
        model = ARInvoiceInfo
        fields = ['deliveryNo','salesOrder','customerName','docNo','address' ,'totalQty','totalAmount','sales_employee']
        widgets = {
            'docNo': forms.TextInput(attrs={'readonly': 'readonly'}),
            'totalAmount': forms.TextInput(attrs={'readonly': 'readonly'}),
            'totalQty': forms.TextInput(attrs={'readonly': 'readonly'}),
            # 'customerName': ModelSelect2Widget(model=BusinessPartner, search_fields=['name__icontains']),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not self.instance.pk:
            last_invoice = ARInvoiceInfo.objects.order_by('-docNo').first()
            if last_invoice:
                next_invoice_number = last_invoice.docNo + 1
            else:
                next_invoice_number = 1

            self.initial['docNo'] = next_invoice_number

@admin.register(ARInvoiceInfo)
class ARInvoiceInfoAdmin(admin.ModelAdmin):
    form = ARInvoiceInfoAdminForm
    inlines = [ARInvoiceItemInline]
    change_form_template = 'admin/erp/change_form.html'     

    class Media:
        js = ('js/arinvoice.js',)
        defer = True
        css = {
            'all': ('css/bootstrap.min.css','css/admin_styles.css'),
        } 
    def save_model(self, request, obj, form, change):
        if not obj.address:
            if obj.customerName:
                obj.address = obj.customerName.address
        obj.owner = request.user if request.user.is_authenticated else None              
        super().save_model(request, obj, form, change)
                
                
                
                
           
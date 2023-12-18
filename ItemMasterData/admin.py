from django.contrib import admin

from django import forms
from .models import  ItemGroup,Item

@admin.register(ItemGroup)
class ItemGroupAdmin(admin.ModelAdmin):
    list_display = ('name',  'description')
           
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('code','name',  'description')
    search_fields = ('name',) 
    fields = ['code','name','unit','item_group']  

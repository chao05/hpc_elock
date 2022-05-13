from django.contrib import admin
from .models import AKC, AddonGeneral

class AKCAdmin(admin.ModelAdmin):
    list_display=('serial_number','addon', 'salesman', 'client', 'po_number')
    search_fields=list_display
    list_filter=('salesman', 'client')

class AddonGeneralAdmin(admin.ModelAdmin):
    list_display=('code', 'desc')
    search_fields=list_display

admin.site.register(AKC, AKCAdmin)
admin.site.register(AddonGeneral, AddonGeneralAdmin)

from django.contrib import admin
from .models import EquipmentCategory
#Equipment Admin View
class EquipmentCayegoryAdmin(admin.ModelAdmin):
    list_display('category_name','date_created',)#Display Data in 
    list_filter=('date_created',)
    search_fields=('category_name',)#Add A search Field











#register Models
admin.site.register(EquipmentCategory,EquipmentCategoryAdmin)
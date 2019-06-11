from django.contrib import admin
from user.models import UserProfile, EmployeeProfile, InventoryProfile, InventoryCountProfile, ForcastedSalesProfile, ActualSalesProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'employee_number')

    def user_info(self, obj):
        return obj.user


class EmployeeProfileAdmin(admin.ModelAdmin):
    list_display = ('first', 'last', 'employee_number', 'pay')


class InventoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'sku', 'category', 'case', 'serving_yield', 'serving_size', 'unit', 'quantity', 'price')
    search_fields = ('name', 'sku', 'category', 'company')
    list_editable = ('case', 'category', 'serving_yield', 'serving_size', 'unit', 'quantity')


class ActualSalesProfileAdmin(admin.ModelAdmin):
    list_display = ('date_start', 'date_end', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'total')


class ForcastedSalesAdmin(admin.ModelAdmin):
    list_display = ('date_start', 'date_end', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'total')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(EmployeeProfile, EmployeeProfileAdmin)
admin.site.register(InventoryProfile, InventoryAdmin)
admin.site.register(InventoryCountProfile)
admin.site.register(ActualSalesProfile, ActualSalesProfileAdmin)
admin.site.register(ForcastedSalesProfile, ForcastedSalesAdmin)

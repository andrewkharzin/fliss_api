from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models.customer import Customer
from .models.role import Role
from .models.permission import Permission

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'is_staff', 'is_superuser')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name')
    search_fields = ('id', 'company_name')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Role)
admin.site.register(Permission)
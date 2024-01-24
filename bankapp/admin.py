from django.contrib import admin
from .models import District,Branches,AccountType,Userdetails,Materials
# Register your models here.

class AdminDistrict(admin.ModelAdmin):
    list_display = ['id', 'dist_name']

admin.site.register(District,AdminDistrict)

class AdmnBranches(admin.ModelAdmin):
    list_display = ['id','branch_name','district_name']

admin.site.register(Branches,AdmnBranches)

class AdminAccount(admin.ModelAdmin):
    list_display = ['id', 'name']

admin.site.register(AccountType,AdminAccount)

class AdminUserdetails(admin.ModelAdmin):
    list_display = ['id', 'name', 'dob', 'age', 'gender', 'phone_number', 'email', 'address', 'district', 'branch', 'account_type', 'materials','materials_provide']
    list_per_page = 5
admin.site.register(Userdetails, AdminUserdetails)

admin.site.register(Materials)
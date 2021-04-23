from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import Account

class Accountadmin(UserAdmin):
    list_display = ('is_active','date_joined','username','last_login','email')
    search_fields = ('date_joined','username')
    readonly_fields = ('date_joined','last_login')

    filter_horizontal = ()
    list_filter =()
    fieldsets = ()

admin.site.register(Account,Accountadmin) 
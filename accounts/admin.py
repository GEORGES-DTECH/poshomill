from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import Account

class Accountadmin(UserAdmin):
    list_display = ('has_paid','date_joined','phone','username','last_login','select_country')
    search_fields = ('date_joined','phone','username','select_country')
    readonly_fields = ('date_joined','last_login')

    filter_horizontal = ()
    list_filter =()
    fieldsets = ()

admin.site.register(Account,Accountadmin) 
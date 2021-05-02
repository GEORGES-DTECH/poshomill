from django.contrib.auth.models import User
from django.contrib import admin
from .models import Transaction2,Product2,Transactionreport2

admin.site.register(Transaction2)
admin.site.register(Product2)
admin.site.register(Transactionreport2)


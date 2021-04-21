from django.contrib.auth.models import User
from django.contrib import admin
from .models import Transaction,Product,Invoice,Transactionreport,Employee

admin.site.register(Transaction)
admin.site.register(Product)
admin.site.register(Invoice)
admin.site.register(Transactionreport)
admin.site.register(Employee)

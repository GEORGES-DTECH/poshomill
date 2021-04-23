from django.contrib.auth.models import User
from django.contrib import admin
from .models import Transaction,Product,Transactionreport

admin.site.register(Transaction)
admin.site.register(Product)
admin.site.register(Transactionreport)


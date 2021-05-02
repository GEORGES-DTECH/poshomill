from django import forms
from .models import Transaction, Product

class TransactionForm(forms.ModelForm):
 
 
    class Meta:
        model = Transaction
     
        fields = (
        'select_product1',
        'select_product2',
        'select_product3',
        'select_product4',
        'select_product5',  
        'total_selling_price',
        'customer_payment',
        'mode_of_sale',
        
    )

    
    def __init__(self, employee, *args, **kwargs):
 
        super(TransactionForm, self).__init__(*args, **kwargs)

  
class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Transaction
     
        fields = (
        'expense',
        'expense_description',
        'mode_of_payment'
       
    )

    
    def __init__(self, employee, *args, **kwargs):
 
        super(ExpenseForm, self).__init__(*args, **kwargs)

    
class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Transaction
     
        fields = (
        'products_purchased',
        'quantity_purchased',
        'price_per_each',
       
         'units',
        'mode_of_purchase',
        'suppliers_name',
    )
    
    
    def __init__(self, employee, *args, **kwargs):
 
        super(PurchaseForm, self).__init__(*args, **kwargs)
   

class DebtorForm(forms.ModelForm):
    class Meta:
        model = Transaction
     
        fields = (
        'select_product1',
        'select_product2',
        'select_product3',
        'select_product4',
        'select_product5', 
        'credit_sale_price',
        'customers_name',
        'status',
        
    )
    
    def __init__(self, employee, *args, **kwargs):
 
        super(DebtorForm, self).__init__(*args, **kwargs)

    

class CreditorForm(forms.ModelForm):
    class Meta:
        model = Transaction
     
        fields = (
        'products_purchased',
        'credit_purchase_price',
        'quantity',
        'units',
        'status',
        'suppliers_name',
        'amount_paid',
       
    )
    
    def __init__(self, employee, *args, **kwargs):
 
        super(CreditorForm, self).__init__(*args, **kwargs)

    
from django import forms
from .models import Transaction, Product,Employee

class TransactionForm(forms.ModelForm):
 
 
    class Meta:
        model = Transaction
     
        fields = (
        'select_meal1',
        'select_meal2',
        'select_meal3',
        'select_meal4', 
        'total_selling_price',
        'customer_payment',
        'mode_of_sale',
        'staff'
    )

    def __init__(self, employee, *args, **kwargs):
 
        super(TransactionForm, self).__init__(*args, **kwargs)
        self.fields['select_meal1'].queryset = Product.objects.filter(employee=employee)
        self.fields['select_meal2'].queryset = Product.objects.filter(employee=employee)
        self.fields['select_meal3'].queryset = Product.objects.filter(employee=employee)
        self.fields['select_meal4'].queryset = Product.objects.filter(employee=employee)
        self.fields['staff'].queryset = Employee.objects.filter(employee=employee)

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Transaction
     
        fields = (
        'expense',
        'expense_description',
        'staff',
    )

    def __init__(self, employee, *args, **kwargs):
        super(ExpenseForm, self).__init__(*args, **kwargs)
      
        self.fields['staff'].queryset = Employee.objects.filter(employee=employee)

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Transaction
     
        fields = (
        'products_purchased',
        'purchase_price',
        'mode_of_purchase',
        'staff', 
    )

    def __init__(self, employee, *args, **kwargs):
        super(PurchaseForm, self).__init__(*args, **kwargs)
      
        self.fields['staff'].queryset = Employee.objects.filter(employee=employee)

class DebtorForm(forms.ModelForm):
    class Meta:
        model = Transaction
     
        fields = (
        'select_meal1',
        'select_meal2',
        'select_meal3',
        'select_meal4', 
        'credit_sale_price',
        'credit_sale_customers_name',
        'status',
        'staff'
    )

    def __init__(self, employee, *args, **kwargs):
        super(DebtorForm, self).__init__(*args, **kwargs)
        self.fields['select_meal1'].queryset = Product.objects.filter(employee=employee)
        self.fields['select_meal2'].queryset = Product.objects.filter(employee=employee)
        self.fields['select_meal3'].queryset = Product.objects.filter(employee=employee)
        self.fields['select_meal4'].queryset = Product.objects.filter(employee=employee)
        self.fields['staff'].queryset = Employee.objects.filter(employee=employee)


class CreditorForm(forms.ModelForm):
    class Meta:
        model = Transaction
     
        fields = (
        'products_purchased',
        'credit_purchase_price',
        'credit_purchase_suppliers_name',
        'status',
        'staff', 
    )

    def __init__(self, employee, *args, **kwargs):
        super(CreditorForm, self).__init__(*args, **kwargs)
      
        self.fields['staff'].queryset = Employee.objects.filter(employee=employee)
               
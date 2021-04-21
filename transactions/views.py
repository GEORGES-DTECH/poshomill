
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.mixins import (
    PermissionRequiredMixin,
    LoginRequiredMixin,
    UserPassesTestMixin)
from .models import Transaction,Transactionreport,Product,Invoice,Employee
from django.views.generic import( 
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView)
from django.contrib.auth.decorators import login_required
from.forms import TransactionForm,ExpenseForm,PurchaseForm,CreditorForm,DebtorForm


# =====================DETAIL VIEWS===========================
class InvoicedetailView(LoginRequiredMixin,DetailView):
    model = Invoice
    template_name = 'transactions/invoicedetail.html'
    context_object_name = 'invoice'
 
    
    def get_queryset(self):
        employee = self.request.user
        queryset = Invoice.objects.filter(employee=employee)
        return queryset

class SalesdetailView(LoginRequiredMixin,DetailView):
    model = Transaction
    template_name = 'transactions/salesdetail.html'
    context_object_name = 'transaction'
 
    
    def get_queryset(self):
        employee = self.request.user
        queryset = Transaction.objects.filter(employee=employee)
        return queryset

class PurchasedetailView(LoginRequiredMixin,DetailView):
    model = Transaction
    template_name = 'transactions/purchasedetail.html'
    context_object_name = 'transaction'
 
    
    def get_queryset(self):
        employee = self.request.user
        queryset = Transaction.objects.filter(employee=employee)
        return queryset      

class DebtordetailView(LoginRequiredMixin,DetailView):
    model = Transaction
    template_name = 'transactions/debtordetail.html'
    context_object_name = 'transaction'
 
    
    def get_queryset(self):
        employee = self.request.user
        queryset = Transaction.objects.filter(employee=employee)
        return queryset 

class CreditordetailView(LoginRequiredMixin,DetailView):
    model = Transaction
    template_name = 'transactions/creditordetail.html'
    context_object_name = 'transaction'
 
    
    def get_queryset(self):
        employee = self.request.user
        queryset = Transaction.objects.filter(employee=employee)
        return queryset                   
# ===================HOME VIEWS========================================
class IncomeHomeView(LoginRequiredMixin,ListView):
    model = Transaction
    template_name = 'transactions/income.html'
    context_object_name = 'transaction'
    def get_queryset(self):
        employee = self.request.user
        queryset = Transaction.objects.filter(employee=employee)
        return queryset

class HelpView(LoginRequiredMixin,ListView):
    model = Transaction
    template_name = 'transactions/help.html'
    context_object_name = 'transactions'
    


class ReportHome(LoginRequiredMixin,ListView):
    model = Transactionreport
    template_name = 'transactions/reports.html'
    context_object_name = 'reports'
    paginate_by=12
    
    def get_queryset(self):
        employee = self.request.user
        queryset = Transactionreport.objects.filter(employee=employee).order_by('-year')
        return queryset
   

class InvoiceHomeView(LoginRequiredMixin,ListView):
    model = Invoice
    template_name = 'transactions/invoice.html'
    context_object_name = 'invoices'
    paginate_by=10
    def get_queryset(self):
        employee = self.request.user
        queryset = Invoice.objects.filter(employee=employee).order_by('-invoice_date')
        return queryset

class StaffHomeView(LoginRequiredMixin,ListView):
    model = Employee
    template_name = 'transactions/staffhome.html'
    paginate_by = 20
    context_object_name = 'staffs'
  
    
    def get_queryset(self):
        employee = self.request.user
        queryset = Employee.objects.filter(employee=employee)
        return queryset




class ProductHomeView(LoginRequiredMixin,ListView):
    model = Product
    template_name = 'transactions/productshome.html'
    paginate_by = 20
    context_object_name = 'products'
    products = Product.objects.all()
    
    def get_queryset(self):
        employee = self.request.user
        queryset = Product.objects.filter(employee=employee).order_by('-transaction_date')
        return queryset
    



class TransactionHomeView(LoginRequiredMixin,ListView):
    model = Transaction
    template_name = 'transactions/transactionshome.html'
    context_object_name = 'transactions'
    transactions = Transaction.objects.all()
 

    def get_queryset(self):
        employee = self.request.user
        queryset = Transaction.objects.filter(employee=employee)
        return queryset



    
class DailyReportsHomeView(LoginRequiredMixin,ListView):
    model = Transaction
    template_name = 'transactions/dailyreports.html'
    context_object_name = 'transactions'
   
    transactions = Transaction.objects.all()
 

    def get_queryset(self):
        employee = self.request.user
        queryset = Transaction.objects.filter(employee=employee)
        return queryset
       

class SaleView(LoginRequiredMixin,ListView):
    model = Transaction
    template_name = 'transactions/mysales.html'
    context_object_name = 'transactions'
    paginate_by = 5
    transactions = Transaction.objects.all()
                                                  
    
    def get_queryset(self):
    
        employee = self.request.user
        queryset = Transaction.objects.filter(employee=employee).order_by('-transaction_date')
        return queryset
    
    

class PurchaseView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'transactions/mypurchases.html'
    context_object_name = 'transactions'
    paginate_by = 10
    
  
    def get_queryset(self):
        employee = self.request.user
        queryset = Transaction.objects.filter(employee=employee).order_by('-transaction_date')
        return queryset
    

class ExpenseView(LoginRequiredMixin,ListView):
    model = Transaction
    template_name = 'transactions/myexpenses.html'
    context_object_name = 'transactions'
    paginate_by = 10
    transactions = Transaction.objects.all()
    def get_queryset(self):
        employee = self.request.user
        queryset = Transaction.objects.filter(employee=employee).order_by('-transaction_date')
        return queryset
    

class DebtorView(LoginRequiredMixin,ListView):
    model = Transaction
    template_name = 'transactions/mydebtors.html'
    context_object_name = 'transactions'
    paginate_by = 10
    transactions = Transaction.objects.all()
    
    def get_queryset(self):
        employee = self.request.user
        queryset = Transaction.objects.filter(employee=employee).order_by('-transaction_date')
        return queryset
    


class CreditorView(LoginRequiredMixin,ListView):
    model = Transaction
    template_name = 'transactions/mycreditors.html'
    context_object_name = 'transactions'
    paginate_by = 10
    transactions = Transaction.objects.all()
    def get_queryset(self):
        employee = self.request.user
        queryset = Transaction.objects.filter(employee=employee).order_by('-transaction_date')
        return queryset
    
class PerformanceView(LoginRequiredMixin,ListView):
    model = Transaction
    template_name = 'transactions/performance.html'
    context_object_name = 'transactions'
    paginate_by = 5
    transactions = Transaction.objects.all()
    def get_queryset(self):
        employee = self.request.user
        queryset = Transaction.objects.filter(employee=employee).order_by('-transaction_date')
        return queryset

class ReceiptView(LoginRequiredMixin,ListView):
    model = Transaction
    template_name = 'transactions/receipts.html'
    context_object_name = 'receipts'
    paginate_by = 10

    transactions = Transaction.objects.all()
    def get_queryset(self):
        employee = self.request.user
        queryset = Transaction.objects.filter(employee=employee).order_by('-transaction_date')
        return queryset
       

class AccountHomeView(LoginRequiredMixin,ListView):
    model = Transaction
    template_name = 'transactions/accounts.html'


class PaymentHomeView(LoginRequiredMixin,ListView):
    model = Transaction
    template_name = 'transactions/payments.html'   

class CategoryHomeView(LoginRequiredMixin,ListView):
    model = Transaction
    template_name = 'transactions/selections.html'  

class Branches(LoginRequiredMixin,ListView):
    model = Transaction
    template_name = 'transactions/branches.html'  
   

# ======================CREATE VIEWS=======================================

class InvoiceCreateView(LoginRequiredMixin, CreateView):
    model = Invoice
    template_name = 'transactions/invoicecreate.html'
    fields = [
        'invoice_no',
        'due_date',
        'your_business_name',
        'customer_name',
        'description',
        'amount_due',
        'discount',
        'status'
       
    ]

    def form_valid(self, form):
        form.instance.employee = self.request.user
        return super().form_valid(form)

class ReportCreateView(LoginRequiredMixin, CreateView):
    model = Transactionreport
    template_name = 'transactions/create.html'
    fields = [
        'month',
        'total_monthly_sales',
        'total_monthly_purchases',
        'total_monthly_expenses',
    ]

    def form_valid(self, form):
        form.instance.employee = self.request.user
        return super().form_valid(form)

@login_required
def new_expense(request):
    if request.method == 'POST':
 
        form = ExpenseForm(request.user, request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.employee = request.user
            transaction.save()
        
            return redirect('transaction_home')
         
    else:
        form = ExpenseForm(request.user)
    return render(request, 'transactions/expenseform.html', {'form': form})  
   

@login_required
def new_purchase(request):
    if request.method == 'POST':
 
        form = PurchaseForm(request.user, request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.employee = request.user
            transaction.save()
        
            return redirect('transaction_home')
    else:
        form = PurchaseForm(request.user)
    return render(request, 'transactions/purchaseform.html', {'form': form})  


@login_required
def new_creditor(request):
    if request.method == 'POST':
 
        form = CreditorForm(request.user, request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.employee = request.user
            transaction.save()
            return redirect('mycreditors')
        
         
    else:
        form = CreditorForm(request.user)
    return render(request, 'transactions/creditorform.html', {'form': form}) 


class CreateStaff(LoginRequiredMixin,CreateView):
    model=Employee
    template_name = 'transactions/staff-form.html'
    fields=[
       'staff_name',
        'staff_phone',
        'designation',
        'select_branch'
    ]

    def form_valid(self, form):
        form.instance.employee = self.request.user
        return super().form_valid(form)



class CreateProduct(LoginRequiredMixin,CreateView):
    model=Product
    template_name = 'transactions/productcreate.html'
    fields=[
        
        'product',
        'selling_price',
        'quantity',
     
    ]

    def form_valid(self, form):
        form.instance.employee = self.request.user
        return super().form_valid(form)

@login_required
def new_debtor(request):
    if request.method == 'POST':
 
        form = DebtorForm(request.user, request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.employee = request.user
            transaction.save()
            return redirect('mydebtors')
        
         
    else:
        form = DebtorForm(request.user)
    return render(request, 'transactions/debtorform.html', {'form': form}) 


@login_required
def new_transaction(request):
    if request.method == 'POST':
 
        form = TransactionForm(request.user, request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.employee = request.user
            transaction.save()
            return redirect('sale_detail',transaction.id)
        
    else:
        form = TransactionForm(request.user)
    return render(request, 'transactions/transactionform.html', {'form': form}) 

# ==============================UPDATE VIEWS==============================================

class UpdateStaff(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Employee
    template_name = 'transactions/staff-form.html'
    fields=[
        'staff_name',
        'staff_phone',
        'designation',
        'select_branch'
    ]
    
    def form_valid(self, form):
        form.instance.employee= self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        staff=self.get_object()
        if self.request.user == staff.employee:
            return True
        else:
            return False
          
       



class UpdateProduct(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Product
    template_name = 'transactions/productcreate.html'
    fields=[
        
        'product',
        'selling_price',
        'quantity',
    ]
    
    def form_valid(self, form):
        form.instance.employee= self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        product=self.get_object()
        if self.request.user == product.employee:
            return True
        else:
            return False
          
       

class InvoiceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Invoice
    template_name = 'transactions/invoicecreate.html'
    fields = [
        'invoice_no',
        'due_date',
        'your_business_name',
        'customer_name',
        'description',
        'amount_due',
        'discount',
        'status'
    ]
    # form verification

    def form_valid(self, form):
        form.instance.employee = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        invoice=self.get_object()
        if self.request.user == invoice.employee:
            return True
        else:
            return False    
       


class ReportUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Transactionreport
    template_name = 'transactions/create.html'
    fields = [
        'month',
        'total_monthly_sales',
        'total_monthly_purchases',
        'total_monthly_expenses',
        
    ]
    # form verification

    def form_valid(self, form):
        form.instance.employee = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        transaction=self.get_object()
        if self.request.user == transaction.employee:
            return True
        else:
            return False    

class TransactionPurchaseUpdateView(LoginRequiredMixin,  UpdateView):
    model = Transaction
   
    template_name = 'transactions/purchaseform.html'
    fields = (
        'products_purchased',
        'purchase_price',
        'mode_of_purchase',
        'credit_purchase_price',
        'credit_purchase_suppliers_name',
        'status',
        'staff', 
    )
    
    def form_valid(self, form):
        form.instance.employee = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        transaction=self.get_object()
        if self.request.user == transaction.employee:
            return True
        else:
            return False    
       

class TransactionExpenseUpdateView(LoginRequiredMixin,  UpdateView):
    model = Transaction
    template_name = 'transactions/expenseform.html'
    fields = (
        'expense',
        'expense_description',
        'staff',
    )
    
    # form verification

    def form_valid(self, form):
        form.instance.employee = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        transaction=self.get_object()
        if self.request.user == transaction.employee:
            return True
        else:
            return False       
        


class TransactionCreditorView(LoginRequiredMixin,  UpdateView):
    model = Transaction
   
    template_name = 'transactions/creditorform.html'
    fields = (
        'products_purchased',
        'purchase_price',
        'credit_purchase_price',
        'credit_purchase_suppliers_name',
        'status',
        'staff', 
    )
    def form_valid(self, form):
        form.instance.employee = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        transaction=self.get_object()
        if self.request.user == transaction.employee:
            return True
        else:
            return False    
       



class TransactionDebtorView(LoginRequiredMixin,  UpdateView):
    model = Transaction
   
    template_name = 'transactions/debtorform.html'
    fields = (
        'select_meal1',
        'select_meal2',
        'select_meal3',
        'select_meal4', 
        "another_meal_sold",
        'total_selling_price',
        'credit_sale_price',
        'credit_sale_customers_name',
        'status',
        'staff'
    )
    def form_valid(self, form):
        form.instance.employee = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        transaction=self.get_object()
        if self.request.user == transaction.employee:
            return True
        else:
            return False    
       
  
class TransactionUpdateView(LoginRequiredMixin,  UpdateView):
    model = Transaction
   
    template_name = 'transactions/transactionform.html'
    fields = (
        'select_meal1',
        'select_meal2',
        'select_meal3',
        'select_meal4', 
        'total_selling_price',
        'customer_payment',
        'mode_of_sale',
        'staff',
    )
    
    def form_valid(self, form):
        form.instance.employee = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        transaction=self.get_object()
        if self.request.user == transaction.employee:
            return True
        else:
            return False    
       

# ==============================DELETE VIEWS=============================

class ProductDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView,):
    model = Product
    template_name = 'transactions/productdelete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('products')
    # permission_required = ('products.can_delete')
    
    def test_func(self):
        product=self.get_object()
        if self.request.user == product.employee:
            return True
        else:
            return False    
    

class StaffDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView,):
    model = Employee
    template_name = 'transactions/staffdelete.html'
    context_object_name = 'staff'
    success_url = reverse_lazy('staffs')
    
    
    def test_func(self):
        staff=self.get_object()
        if self.request.user == staff.employee:
            return True
        else:
            return False    
       


class InvoiceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView,):
    model = Invoice
    template_name = 'transactions/invoice_delete.html'
    context_object_name = 'report'
    success_url = reverse_lazy('invoice_home')
   
    def test_func(self):
        invoice=self.get_object()
        if self.request.user == invoice.employee:
            return True
        else:
            return False    
       

class TransactionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView,):
    model = Transaction
    template_name = 'transactions/transaction_confirm_delete.html'
    context_object_name = 'transaction'
    success_url = reverse_lazy('transaction_home')
   
    def test_func(self):
        transaction=self.get_object()
        return True
         

class ReportDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView,):
    model = Transactionreport
    template_name = 'transactions/report_delete.html'
    context_object_name = 'report'
    success_url = reverse_lazy('reports_home')
    # permission_required = ('reports.can_delete')
    def test_func(self):
        transaction=self.get_object()
        if self.request.user == transaction.employee:
            return True
        else:
            return False    
       

class SearchResultView(ListView):
    model = Transactionreport
    context_object_name = 'report'
    template_name = 'transactions/reports.html'

    def get_queryset(self):
        employee = self.request.user
        query = self.request.GET.get('q')
        object_list = Transactionreport.objects.filter(
             Q(month__icontains=query))
        return object_list.filter(employee=employee)

# ===========================SEARCH VIEWS=========================================

class InvoiceSearchResultView(ListView):
    model = Invoice
    context_object_name = 'invoice'
    template_name = 'transactions/invoice.html'
    
   
    def get_queryset(self):
        employee = self.request.user
        query = self.request.GET.get('q')
        object_list = Invoice.objects.filter(
            Q(invoice_no__icontains=query)| Q(customer_name__icontains=query)
            |Q(status__icontains=query))
        return object_list.filter(employee=employee)

class TransactionSearchResultView(ListView):
    model = Transaction
    context_object_name = 'receipt'
    template_name = 'transactions/receipts.html'
    
   
    def get_queryset(self):
        employee = self.request.user
        query = self.request.GET.get('q')
        object_list = Transaction.objects.filter(
            Q(transaction_date__icontains=query)
            )
          
        return object_list.filter(employee=employee).order_by('-transaction_date')
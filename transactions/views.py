
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.mixins import (
    PermissionRequiredMixin,
    LoginRequiredMixin,
    UserPassesTestMixin)
from .models import Transaction,Transactionreport,Product
from django.views.generic import( 
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView)
from django.contrib.auth.decorators import login_required
from.forms import TransactionForm,ExpenseForm,PurchaseForm,CreditorForm,DebtorForm


# =====================DETAIL VIEWS===========================

class SalesdetailView(LoginRequiredMixin,DetailView):
    model = Transaction
    template_name = 'transactions/salesdetail.html'
    context_object_name = 'transaction'
 
    
    

class PurchasedetailView(LoginRequiredMixin,DetailView):
    model = Transaction
    template_name = 'transactions/purchasedetail.html'
    context_object_name = 'transaction'
 
    
        

class DebtordetailView(LoginRequiredMixin,DetailView):
    model = Transaction
    template_name = 'transactions/debtordetail.html'
    context_object_name = 'transaction'
 
    
   

class CreditordetailView(LoginRequiredMixin,DetailView):
    model = Transaction
    template_name = 'transactions/creditordetail.html'
    context_object_name = 'transaction'
 
               
# ===================HOME VIEWS========================================
class IncomeHomeView(LoginRequiredMixin,ListView):
    model = Transaction
    template_name = 'transactions/income.html'
    context_object_name = 'transaction'
  

class HelpView(LoginRequiredMixin,ListView):
    model = Transaction
    template_name = 'transactions/help.html'
    context_object_name = 'transactions'
    


class ReportHome(LoginRequiredMixin,ListView):
    model = Transactionreport
    template_name = 'transactions/reports.html'
    context_object_name = 'reports'
    paginate_by=12
    
   


class ProductHomeView(LoginRequiredMixin,ListView):
    model = Product
    template_name = 'transactions/productshome.html'
    paginate_by = 20
    context_object_name = 'products'
    products = Product.objects.all()
    
  
    



class TransactionHomeView(LoginRequiredMixin,ListView):
    model = Transaction
    template_name = 'transactions/transactionshome.html'
    context_object_name = 'transactions'
    transactions = Transaction.objects.all()
 

   


    
class DailyReportsHomeView(LoginRequiredMixin,ListView):
    model = Transaction
    template_name = 'transactions/dailyreports.html'
    context_object_name = 'transactions'
   
    transactions = Transaction.objects.all()
 

   
       

class SaleView(LoginRequiredMixin,ListView):
    model = Transaction
    template_name = 'transactions/mysales.html'
    context_object_name = 'transactions'
    paginate_by = 5
    transactions = Transaction.objects.all()
                                                  
    
    
    

class PurchaseView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'transactions/mypurchases.html'
    context_object_name = 'transactions'
    paginate_by = 10
    

class StockView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'transactions/stock.html'
    context_object_name = 'transactions'
    paginate_by = 10
    
  
    

class ExpenseView(LoginRequiredMixin,ListView):
    model = Transaction
    template_name = 'transactions/myexpenses.html'
    context_object_name = 'transactions'
    paginate_by = 10
    transactions = Transaction.objects.all()
   

class DebtorView(LoginRequiredMixin,ListView):
    model = Transaction
    template_name = 'transactions/mydebtors.html'
    context_object_name = 'transactions'
    paginate_by = 10
    transactions = Transaction.objects.all()
    
   
    


class CreditorView(LoginRequiredMixin,ListView):
    model = Transaction
    template_name = 'transactions/mycreditors.html'
    context_object_name = 'transactions'
    paginate_by = 10
    transactions = Transaction.objects.all()
   
class PerformanceView(LoginRequiredMixin,ListView):
    model = Transaction
    template_name = 'transactions/performance.html'
    context_object_name = 'transactions'
    paginate_by = 5
    transactions = Transaction.objects.all()
  
class ReceiptView(LoginRequiredMixin,ListView):
    model = Transaction
    template_name = 'transactions/receipts.html'
    context_object_name = 'receipts'
    paginate_by = 10

    transactions = Transaction.objects.all()
   
       

class AccountHomeView(LoginRequiredMixin,ListView):
    model = Transaction
    template_name = 'transactions/accounts.html'




class Branches(LoginRequiredMixin,ListView):
    model = Transaction
    template_name = 'transactions/branches.html'  
   

# ======================CREATE VIEWS=======================================



class ReportCreateView(LoginRequiredMixin, CreateView):
    model = Transactionreport
    template_name = 'transactions/create.html'
    fields = [
        'month',
        'total_monthly_sales',
        'total_monthly_processed_goods',
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
 
    
    

class ReportUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Transactionreport
    template_name = 'transactions/create.html'
    fields = [
        'month',
        'total_monthly_sales',
        'total_monthly_processed_goods',
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
        'quantity_purchased',
        'price_per_each',
        'quantity_used',
         'units',
        'mode_of_purchase',
        'suppliers_name',
        
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
        'credit_purchase_price',
        'quantity_purchased',
        'quantity_used',
         'units',
         'status',
        'suppliers_name',
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
        'select_product1',
        'select_product2',
        'select_product3',
        'select_product4',
        'select_product5', 
        'credit_sale_price',
        'customers_name',
        'status',
        
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
        'select_product1',
        'select_product2',
        'select_product3',
        'select_product4',
        'select_product5',  
        'total_selling_price',
        'customer_payment',
        'mode_of_sale',
        
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
        
        query = self.request.GET.get('q')
        object_list = Transactionreport.objects.filter(
             Q(month__icontains=query))
        return object_list

# ===========================SEARCH VIEWS=========================================


class TransactionSearchResultView(ListView):
    model = Transaction
    context_object_name = 'receipt'
    template_name = 'transactions/receipts.html'
    
   
    def get_queryset(self):
     
        query = self.request.GET.get('q')
        object_list = Transaction.objects.filter(
            Q(transaction_date__icontains=query)
            )
          
        return object_list.order_by('-transaction_date')
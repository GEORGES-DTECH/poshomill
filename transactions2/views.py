
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.mixins import (
    PermissionRequiredMixin,
    LoginRequiredMixin,
    UserPassesTestMixin)
from .models import Transaction2,Transactionreport2,Product2
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
    model = Transaction2
    template_name = 'transactions2/salesdetail.html'
    context_object_name = 'transaction'
 
    
    

class PurchasedetailView(LoginRequiredMixin,DetailView):
    model = Transaction2
    template_name = 'transactions2/purchasedetail.html'
    context_object_name = 'transaction'
 
    
        

class DebtordetailView(LoginRequiredMixin,DetailView):
    model = Transaction2
    template_name = 'transactions2/debtordetail.html'
    context_object_name = 'transaction'
 
    
   

class CreditordetailView(LoginRequiredMixin,DetailView):
    model = Transaction2
    template_name = 'transactions2/creditordetail.html'
    context_object_name = 'transaction'
 
               
# ===================HOME VIEWS========================================
class IncomeHomeView(LoginRequiredMixin,ListView):
    model = Transaction2
    template_name = 'transactions2/income.html'
    context_object_name = 'transaction'
  


    


class ReportHome(LoginRequiredMixin,ListView):
    model = Transactionreport2
    template_name = 'transactions2/reports.html'
    context_object_name = 'reports'
    paginate_by=12
    
   


class ProductHomeView(LoginRequiredMixin,ListView):
    model = Product2
    template_name = 'transactions2/productshome.html'
    paginate_by = 20
    context_object_name = 'products'
    products = Product2.objects.all()
    
  
    



class TransactionHomeView(LoginRequiredMixin,ListView):
    model = Transaction2
    template_name = 'transactions2/transactionshome.html'
    context_object_name = 'transactions'
    transactions = Transaction2.objects.all()
 

   


    
class DailyReportsHomeView(LoginRequiredMixin,ListView):
    model = Transaction2
    template_name = 'transactions2/dailyreports.html'
    context_object_name = 'transactions'
   
    transactions = Transaction2.objects.all()
 

   
       

class SaleView(LoginRequiredMixin,ListView):
    model = Transaction2
    template_name = 'transactions2/mysales.html'
    context_object_name = 'transactions'
    paginate_by = 5
    transactions = Transaction2.objects.all()
                                                  
    
    
    

class PurchaseView(LoginRequiredMixin, ListView):
    model = Transaction2
    template_name = 'transactions2/mypurchases.html'
    context_object_name = 'transactions'
    paginate_by = 10
    

class StockView(LoginRequiredMixin, ListView):
    model = Transaction2
    template_name = 'transactions2/stock.html'
    context_object_name = 'transactions'
    paginate_by = 10
    
  
    

class ExpenseView(LoginRequiredMixin,ListView):
    model = Transaction2
    template_name = 'transactions2/myexpenses.html'
    context_object_name = 'transactions'
    paginate_by = 10
    transactions = Transaction2.objects.all()
   

class DebtorView(LoginRequiredMixin,ListView):
    model = Transaction2
    template_name = 'transactions2/mydebtors.html'
    context_object_name = 'transactions'
    paginate_by = 10
    transactions = Transaction2.objects.all()
    
   
    


class CreditorView(LoginRequiredMixin,ListView):
    model = Transaction2
    template_name = 'transactions2/mycreditors.html'
    context_object_name = 'transactions'
    paginate_by = 10
    transactions = Transaction2.objects.all()
   
class PerformanceView(LoginRequiredMixin,ListView):
    model = Transaction2
    template_name = 'transactions2/performance.html'
    context_object_name = 'transactions'
    paginate_by = 5
    transactions = Transaction2.objects.all()
  
class ReceiptView(LoginRequiredMixin,ListView):
    model = Transaction2
    template_name = 'transactions2/receipts.html'
    context_object_name = 'receipts'
    paginate_by = 10

    transactions = Transaction2.objects.all()
   
       

class AccountHomeView(LoginRequiredMixin,ListView):
    model = Transaction2
    template_name = 'transactions2/accounts.html'

# ======================CREATE VIEWS=======================================

class ReportCreateView(LoginRequiredMixin, CreateView):
    model = Transactionreport2
    template_name = 'transactions2/create.html'
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
        
            return redirect('2transaction_home')
         
    else:
        form = ExpenseForm(request.user)
    return render(request, 'transactions2/expenseform.html', {'form': form})  
   

@login_required
def new_purchase(request):
    if request.method == 'POST':
 
        form = PurchaseForm(request.user, request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.employee = request.user
            transaction.save()
        
            return redirect('2mypurchases')
    else:
        form = PurchaseForm(request.user)
    return render(request, 'transactions2/purchaseform.html', {'form': form})  


@login_required
def new_creditor(request):
    if request.method == 'POST':
 
        form = CreditorForm(request.user, request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.employee = request.user
            transaction.save()
            return redirect('2mycreditors')
        
         
    else:
        form = CreditorForm(request.user)
    return render(request, 'transactions2/creditorform.html', {'form': form}) 




class CreateProduct(LoginRequiredMixin,CreateView):
    model=Product2
    template_name = 'transactions2/productcreate.html'
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
            return redirect('2mydebtors')
        
         
    else:
        form = DebtorForm(request.user)
    return render(request, 'transactions2/debtorform.html', {'form': form}) 


@login_required
def new_transaction(request):
    if request.method == 'POST':
 
        form = TransactionForm(request.user, request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.employee = request.user
            transaction.save()
            return redirect('2sale_detail',transaction.id)
        
    else:
        form = TransactionForm(request.user)
    return render(request, 'transactions2/transactionform.html', {'form': form}) 

# ==============================UPDATE VIEWS==============================================

class UpdateStock(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Transaction2
    template_name = 'transactions2/stockupdate.html'
    fields=[
        
  'products_purchased',
   'quantity_used',
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
 
    
class UpdateProduct(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Product2
    template_name = 'transactions2/productcreate.html'
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
    model = Transactionreport2
    template_name = 'transactions2/create.html'
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
    model = Transaction2
   
    template_name = 'transactions2/purchaseform.html'
    fields = (
        'products_purchased',
        'quantity_purchased',
        'price_per_each',
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
    model = Transaction2
    template_name = 'transactions2/expenseform.html'
    fields = (
        'expense',
        'expense_description',
        'mode_of_payment'
        
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
        


class TransactionCreditorView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Transaction2
   
    template_name = 'transactions2/creditorform.html'
    fields = (
         'products_purchased',
        'credit_purchase_price',
         'quantity',
         'units',
         'status',
         'amount_paid',
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
    model = Transaction2
   
    template_name = 'transactions2/debtorform.html'
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
    model = Transaction2
   
    template_name = 'transactions2/transactionform.html'
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
    model = Product2
    template_name = 'transactions2/productdelete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('2products')
    # permission_required = ('products.can_delete')
    
    def test_func(self):
        product=self.get_object()
        if self.request.user == product.employee:
            return True
        else:
            return False    
    

class TransactionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView,):
    model = Transaction2
    template_name = 'transactions/transaction_confirm_delete.html'
    context_object_name = 'transaction'
    success_url = reverse_lazy('2transaction_home')
   
    def test_func(self):
        transaction=self.get_object()
        return True
         

class ReportDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView,):
    model = Transactionreport2
    template_name = 'transactions2/report_delete.html'
    context_object_name = 'report'
    success_url = reverse_lazy('2reports_home')
    # permission_required = ('reports.can_delete')
    def test_func(self):
        transaction=self.get_object()
        if self.request.user == transaction.employee:
            return True
        else:
            return False    
       

class SearchResultView(ListView):
    model = Transactionreport2
    context_object_name = 'report'
    template_name = 'transactions2/reports.html'

    def get_queryset(self):
        
        query = self.request.GET.get('q')
        object_list = Transactionreport2.objects.filter(
             Q(month__icontains=query))
        return object_list

# ===========================SEARCH VIEWS=========================================


class TransactionSearchResultView(ListView):
    model = Transaction2
    context_object_name = 'receipt'
    template_name = 'transactions2/receipts.html'
    
   
    def get_queryset(self):
     
        query = self.request.GET.get('q')
        object_list = Transaction2.objects.filter(
            Q(transaction_date__icontains=query)
            )
          
        return object_list.order_by('-transaction_date')
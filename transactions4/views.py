
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.mixins import (
    PermissionRequiredMixin,
    LoginRequiredMixin,
    UserPassesTestMixin)
from .models import Transaction4,Transactionreport4,Product4
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
    model = Transaction4
    template_name = 'transactions4/salesdetail.html'
    context_object_name = 'transaction'
 
    
    

class PurchasedetailView(LoginRequiredMixin,DetailView):
    model = Transaction4
    template_name = 'transactions4/purchasedetail.html'
    context_object_name = 'transaction'
 
    
        

class DebtordetailView(LoginRequiredMixin,DetailView):
    model = Transaction4
    template_name = 'transactions4/debtordetail.html'
    context_object_name = 'transaction'
 
    
   

class CreditordetailView(LoginRequiredMixin,DetailView):
    model = Transaction4
    template_name = 'transactions4/creditordetail.html'
    context_object_name = 'transaction'
 
               
# ===================HOME VIEWS========================================
class IncomeHomeView(LoginRequiredMixin,ListView):
    model = Transaction4
    template_name = 'transactions4/income.html'
    context_object_name = 'transaction'
  


    


class ReportHome(LoginRequiredMixin,ListView):
    model = Transactionreport4
    template_name = 'transactions4/reports.html'
    context_object_name = 'reports'
    paginate_by=12
    
   


class ProductHomeView(LoginRequiredMixin,ListView):
    model = Product4
    template_name = 'transactions4/productshome.html'
    paginate_by = 20
    context_object_name = 'products'
    products = Product4.objects.all()
    
  
    



class TransactionHomeView(LoginRequiredMixin,ListView):
    model = Transaction4
    template_name = 'transactions4/transactionshome.html'
    context_object_name = 'transactions'
    transactions = Transaction4.objects.all()
 

   


    
class DailyReportsHomeView(LoginRequiredMixin,ListView):
    model = Transaction4
    template_name = 'transactions4/dailyreports.html'
    context_object_name = 'transactions'
   
    transactions = Transaction4.objects.all()
 

   
       

class SaleView(LoginRequiredMixin,ListView):
    model = Transaction4
    template_name = 'transactions4/mysales.html'
    context_object_name = 'transactions'
    paginate_by = 5
    transactions = Transaction4.objects.all()
                                                  
    
    
    

class PurchaseView(LoginRequiredMixin, ListView):
    model = Transaction4
    template_name = 'transactions4/mypurchases.html'
    context_object_name = 'transactions'
    paginate_by = 10
    

class StockView(LoginRequiredMixin, ListView):
    model = Transaction4
    template_name = 'transactions4/stock.html'
    context_object_name = 'transactions'
    paginate_by = 10
    
  
    

class ExpenseView(LoginRequiredMixin,ListView):
    model = Transaction4
    template_name = 'transactions4/myexpenses.html'
    context_object_name = 'transactions'
    paginate_by = 10
    transactions = Transaction4.objects.all()
   

class DebtorView(LoginRequiredMixin,ListView):
    model = Transaction4
    template_name = 'transactions4/mydebtors.html'
    context_object_name = 'transactions'
    paginate_by = 10
    transactions = Transaction4.objects.all()
    
   
    


class CreditorView(LoginRequiredMixin,ListView):
    model = Transaction4
    template_name = 'transactions4/mycreditors.html'
    context_object_name = 'transactions'
    paginate_by = 10
    transactions = Transaction4.objects.all()
   
class PerformanceView(LoginRequiredMixin,ListView):
    model = Transaction4
    template_name = 'transactions4/performance.html'
    context_object_name = 'transactions'
    paginate_by = 5
    transactions = Transaction4.objects.all()
  
class ReceiptView(LoginRequiredMixin,ListView):
    model = Transaction4
    template_name = 'transactions4/receipts.html'
    context_object_name = 'receipts'
    paginate_by = 10

    transactions = Transaction4.objects.all()
   
       

class AccountHomeView(LoginRequiredMixin,ListView):
    model = Transaction4
    template_name = 'transactions4/accounts.html'

# ======================CREATE VIEWS=======================================

class ReportCreateView(LoginRequiredMixin, CreateView):
    model = Transactionreport4
    template_name = 'transactions4/create.html'
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
        
            return redirect('4transaction_home')
         
    else:
        form = ExpenseForm(request.user)
    return render(request, 'transactions4/expenseform.html', {'form': form})  
   

@login_required
def new_purchase(request):
    if request.method == 'POST':
 
        form = PurchaseForm(request.user, request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.employee = request.user
            transaction.save()
        
            return redirect('4mypurchases')
    else:
        form = PurchaseForm(request.user)
    return render(request, 'transactions4/purchaseform.html', {'form': form})  


@login_required
def new_creditor(request):
    if request.method == 'POST':
 
        form = CreditorForm(request.user, request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.employee = request.user
            transaction.save()
            return redirect('4mycreditors')
        
         
    else:
        form = CreditorForm(request.user)
    return render(request, 'transactions4/creditorform.html', {'form': form}) 




class CreateProduct(LoginRequiredMixin,CreateView):
    model=Product4
    template_name = 'transactions4/productcreate.html'
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
            return redirect('4mydebtors')
        
         
    else:
        form = DebtorForm(request.user)
    return render(request, 'transactions4/debtorform.html', {'form': form}) 


@login_required
def new_transaction(request):
    if request.method == 'POST':
 
        form = TransactionForm(request.user, request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.employee = request.user
            transaction.save()
            return redirect('4sale_detail',transaction.id)
        
    else:
        form = TransactionForm(request.user)
    return render(request, 'transactions4/transactionform.html', {'form': form}) 

# ==============================UPDATE VIEWS==============================================

class UpdateStock(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Transaction4
    template_name = 'transactions4/stockupdate.html'
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
    model=Product4
    template_name = 'transactions4/productcreate.html'
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
    model = Transactionreport4
    template_name = 'transactions4/create.html'
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
    model = Transaction4
   
    template_name = 'transactions4/purchaseform.html'
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
    model = Transaction4
    template_name = 'transactions4/expenseform.html'
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
    model = Transaction4
   
    template_name = 'transactions4/creditorform.html'
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
    model = Transaction4
   
    template_name = 'transactions4/debtorform.html'
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
    model = Transaction4
   
    template_name = 'transactions4/transactionform.html'
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
    model = Product4
    template_name = 'transactions4/productdelete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('4products')
    # permission_required = ('products.can_delete')
    
    def test_func(self):
        product=self.get_object()
        if self.request.user == product.employee:
            return True
        else:
            return False    
    

class TransactionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView,):
    model = Transaction4
    template_name = 'transactions4/transaction_confirm_delete.html'
    context_object_name = 'transaction'
    success_url = reverse_lazy('4transaction_home')
   
    def test_func(self):
        transaction=self.get_object()
        return True
         

class ReportDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView,):
    model = Transactionreport4
    template_name = 'transactions4/report_delete.html'
    context_object_name = 'report'
    success_url = reverse_lazy('4reports_home')
    # permission_required = ('reports.can_delete')
    def test_func(self):
        transaction=self.get_object()
        if self.request.user == transaction.employee:
            return True
        else:
            return False    
       

class SearchResultView(ListView):
    model = Transactionreport4
    context_object_name = 'report'
    template_name = 'transactions4/reports.html'

    def get_queryset(self):
        
        query = self.request.GET.get('q')
        object_list = Transactionreport4.objects.filter(
             Q(month__icontains=query))
        return object_list

# ===========================SEARCH VIEWS=========================================


class TransactionSearchResultView(ListView):
    model = Transaction4
    context_object_name = 'receipt'
    template_name = 'transactions4/receipts.html'
    
   
    def get_queryset(self):
     
        query = self.request.GET.get('q')
        object_list = Transaction4.objects.filter(
            Q(transaction_date__icontains=query)
            )
          
        return object_list.order_by('-transaction_date')
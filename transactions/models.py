from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from django.utils.functional import cached_property
from django.db.models import Sum,Count
from django.utils import timezone
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta
import calendar


class Employee(models.Model):
    BRANCHES= (
        ('ONE', 'ONE'),
        ('TWO', 'TWO'),
        ('THREE', 'THREE'),
         ('FOUR', 'FOUR'),
        ('FIVE', 'FIVE'),
        
    )

    staff_name=models.CharField(max_length=100,null=True,blank=True)
    staff_phone=models.CharField(max_length=100,null=True,blank=True)
    designation=models.CharField(max_length=100,null=True,blank=True)
    select_branch=models.CharField(max_length=100,null=True,blank=True,choices=BRANCHES)
    employee=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("staff_create")
    
    def __str__(self): 
        return self.staff_name


class Product(models.Model):
    product=models.CharField(max_length=200,null=True,blank=True)
    quantity=models.IntegerField(default=1)
    selling_price=models.IntegerField(null=True)
    employee=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    transaction_date = models.DateTimeField(default=timezone.now)
    
    def get_absolute_url(self):
        return reverse("product_create")
    
    def __str__(self): 
        return self.product + " @ " + '' + str(self.selling_price)
      
    

class TransactionManager(models.Manager):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.select_related('employee')
     
class Transaction(models.Model):
   
    MODE= (
        ('Cash', 'Cash'),
        ('Mpesa', 'Mpesa'),
        ('Bank', 'Bank'),
        
    )

    MODEPURCHASE= (
        ('Cash', 'Cash'),
        ('Mpesa', 'Mpesa'),
        ('Bank', 'Bank'),
        
    )

    STATUS= (
        ('paid', 'paid'),
        ('unpaid', 'unpaid'),
       
        
    )
    DESCRIPTION= (
        
        ('rent', 'rent'),
        ('wages', 'wages'),
        ('other', 'other'),
        ('water', 'water'),
        ('electricity', 'electricity'),
        ('withdrawal', 'withdrawal'),
        ('license fee', 'license fee'),
        ('business permit', 'business permit'),
    )
   
    total_selling_price=models.IntegerField(null=True)
   
    mode_of_sale=models.CharField(choices=MODE,max_length=100,default="cash")
    purchase_price = models.IntegerField(default=0)
    mode_of_purchase=models.CharField(choices=MODEPURCHASE,max_length=100,default="cash")
    expense= models.IntegerField(default=0)
    customer_payment= models.IntegerField(null=True,blank=True)
    expense_description = models.CharField(choices=DESCRIPTION,max_length=100,default="")
    credit_sale_price = models.IntegerField(default=0)
    credit_purchase_price = models.IntegerField(default=0)
    credit_sale_customers_name = models.CharField(max_length=100,blank=True)
    credit_purchase_suppliers_name = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=50,choices=STATUS,default="unpaid")
    transaction_date = models.DateTimeField(default=timezone.now)
    employee=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    staff = models.ForeignKey(Employee,related_name="transactions",on_delete=models.CASCADE,null=True)
    select_meal1=models.ForeignKey(Product,related_name="transactions1",on_delete=models.CASCADE,null=True,blank=True)
    select_meal2=models.ForeignKey(Product,related_name="transactions2",on_delete=models.CASCADE,null=True,blank=True)
    select_meal3=models.ForeignKey(Product,related_name="transactions3",on_delete=models.CASCADE,null=True,blank=True)
    select_meal4=models.ForeignKey(Product,related_name="transactions4",on_delete=models.CASCADE,null=True,blank=True)
    products_purchased = models.CharField(max_length=100, blank=True,default="")
    objects = TransactionManager()
    
    
  
 
    def __str__(self): 
        return self.employee

    def get_absolute_url(self):
        return reverse('transaction_home')
        # return reverse ("sale_detail",kwargs={'pk':self.pk})
       
    
    @cached_property
    def sale_condition(self):
        self.total_selling_price = 0
        return self.total_selling_price
    
    @cached_property
    def change(self):
        if self.customer_payment is None:
            self.customer_payment = 0
         
        return self.customer_payment - self.total_selling_price    
    

# ========================CUMULATIVE REPORTS===================================================================


    @cached_property
    def the_date_today(self):
        now = datetime.now()
        return now
    
    @cached_property
    def the_day_today(self):
        now = datetime.now()
        return  calendar.day_name[now.weekday()] 
    
    @cached_property
    def the_day(self):
        date = self.transaction_date
        return calendar.day_name[date.weekday()]

    
       
    @cached_property
    def total_credit_sales(self):
        result= Transaction.objects.filter(employee=self.employee).filter(status="unpaid")\
            .aggregate(total=Sum('credit_sale_price'))
        return result[ 'total']
    
    
    @cached_property
    def total_credit_purchases(self):
        result= Transaction.objects.filter(employee=self.employee).filter(status="unpaid")\
            .aggregate(total=Sum('credit_purchase_price'))
        return result[ 'total']
    


    @cached_property
    def total_purchases(self):
        result= Transaction.objects.filter(employee=self.employee).aggregate(total=Sum('purchase_price'))
        return result[ 'total']
    

    @cached_property
    def total_expense(self):
        result= Transaction.objects.filter(employee=self.employee).aggregate(total=Sum('expense'))
        return result[ 'total']
    
    @cached_property
    def total_sales_amount(self):
    
  
      result= Transaction.objects.filter(employee=self.employee).aggregate(total=Sum('total_selling_price'))
      return result[ 'total']
    
   




    # =============sales confirmation===========================
    @cached_property
    def saleconfirmation(self):
        if self.total_selling_price is None:
            self.total_selling_price = 0
        if self.total_selling_price > 0:
            return self.total_selling_price
        
    
    # ====================purchases=====================================
    @cached_property
    def purchaseconfirmation(self):
        if self.purchase_price> 0:
            return self.purchase_price
        

    # ====================expenses=====================================
    @cached_property
    def expenseconfirmation(self):
        if self.expense> 0:
            return self.expense
       

       
# ====================debtors=====================================
    @cached_property
    def debtorconfirmation(self):
        if self.credit_sale_price> 0 and self.status == "unpaid":
            return self.credit_sale_price
       
       
# ====================creditors=====================================
    @cached_property
    def creditorconfirmation(self):
        if self.credit_purchase_price> 0 and self.status=="unpaid":
            return self.credit_purchase_price
       
# ====================creditors=====================================
    @cached_property
    def performanceconfirmation(self):
        if self.select_meal_sold != None:
            return self.sale_price
       
    
    
    
    # ===========================mpesa and cash sale determination===========================
    @cached_property
    def total_mpesa_sales_amount(self):
    
      result= Transaction.objects.filter(employee=self.employee).filter(mode_of_sale="Mpesa")\
          .aggregate(total=Sum('total_selling_price'))
      return result[ 'total']
    
    @cached_property
    def total_cash_sales_amount(self):
    
      result= Transaction.objects.filter(employee=self.employee).filter(mode_of_sale="Cash")\
          .aggregate(total=Sum('total_selling_price'))
      return result[ 'total']
    
    @cached_property
    def total_bank_sales_amount(self):
    
      result= Transaction.objects.filter(employee=self.employee).filter(mode_of_sale="Bank")\
          .aggregate(total=Sum('total_selling_price'))
      return result[ 'total']
    

       # ===========================mpesa and cash purchase determination===========================
    @cached_property
    def total_mpesa_purchase_amount(self):
    
      result= Transaction.objects.filter(employee=self.employee).filter(mode_of_purchase="Mpesa")\
          .aggregate(total=Sum('purchase_price'))
      return result[ 'total']
    
    @cached_property
    def total_cash_purchase_amount(self):
    
      result= Transaction.objects.filter(employee=self.employee).filter(mode_of_purchase="Cash")\
          .aggregate(total=Sum('purchase_price'))
      return result[ 'total']
    
    @cached_property
    def total_bank_purchase_amount(self):
    
      result= Transaction.objects.filter(employee=self.employee).filter(mode_of_purchase="Bank")\
          .aggregate(total=Sum('purchase_price'))
      return result[ 'total']
    
    @cached_property
    def mpesa_balance(self):
        method1=self.total_mpesa_sales_amount
        method2 = self.total_mpesa_purchase_amount
        if method1 is None:
            method1 = 0
        if method2 is None:
            method2 = 0    
        return method1 - method2
    
    
    # ====================cash in hand determination===================
    @cached_property
    def total_cash_in_hand(self):
      
        method3=self.total_expense
        method2=self.total_cash_purchase_amount
        method1=self.total_cash_sales_amount
        if method1 is None:
            method1 = 0
        if method2 is None:
            method2 = 0
        if method3 is None:
            method3 = 0    
       
        result= method1-(method2+method3)
        return result

 
    # ==================================DAILY CUMULATIVE REPORTS==================================
    @cached_property
    def total_daily_sales(self):
      result= Transaction.objects.filter(employee=self.employee)\
          .filter(transaction_date__date=date.today()).aggregate(total=Sum('total_selling_price'))
      return result[ 'total']
    
     

    @cached_property
    def total_daily_purchases(self):
      result= Transaction.objects.filter(employee=self.employee)\
          .filter(transaction_date__date=date.today()).aggregate(total=Sum('purchase_price'))
      return result[ 'total']
    

    @cached_property
    def total_daily_expenses(self):
      result= Transaction.objects.filter(employee=self.employee)\
          .filter(transaction_date__date=date.today()).aggregate(total=Sum('expense'))
      return result[ 'total']
    
    @cached_property
    def total_daily_credit_sales(self):
      result= Transaction.objects.filter(employee=self.employee)\
          .filter(transaction_date__date=date.today()).filter(status="unpaid")\
              .aggregate(total=Sum('credit_sale_price'))
      return result[ 'total']
    
    @cached_property
    def total_daily_credit_purchases(self):
      result= Transaction.objects.filter(employee=self.employee)\
          .filter(transaction_date__date=date.today()).filter(status="unpaid")\
              .aggregate(total=Sum('credit_purchase_price'))
      return result[ 'total']
    
    @cached_property
    def daily_profit(self):
        
        method1= self.total_daily_sales
        method2 = self.total_daily_purchases
        method3 = self.total_daily_expenses
        if method1 != None:
            income = method1 -(method2+method3)
            if income > 0:
                return "A profit of " + str(income)
            elif income==0:
                return "A breakeven of " +str(income)
            else:
                return "A loss of " + str(abs(income))  
        
    
    
   
    # ==============total sales and expense in income statement============
    @cached_property
    def sales_in_income(self):
        method1 = self.total_sales_amount
        
        return method1

    @cached_property
    def expenses(self):
        method1=self.total_expense
        
        return method1
    
    
 #    =======================income calculation===============================================================================================
    @cached_property
    def myincome(self):
        method1 = self.sales_in_income
        method2 = self.total_purchases
        method3=self.expenses
        if method1 is None:
            method1 = 0
        if method2 is None:
            method2 = 0
        if method3 is None:
            method3 = 0        
        income=method1-(method2+method3)
        if income>0:
            return "A profit of " + str(income)
        elif income==0:
            return "A breakeven of " +str(income)
        else:
            return "A loss of " + str(abs(income))  
      
    @cached_property
    def revenue(self):
        method1=self.sales_in_income
        method2=self.total_purchases
        if method1 is None:
            method1 = 0
        if method2 is None:
            method2 = 0    
        return method1-method2

    @cached_property
    def profit_margin(self):
        method2 = self.total_purchases
        method3 = self.revenue
        difference = method3 - method2
        if difference >0 or difference < 0: 
            return round(difference/method3 * 100,2)
        if difference == 0:
            return 0    


   
class Transactionreport(models.Model):
    CHOICES=(
        ('Jan','Jan'),
        ('Feb', 'Feb'),
        ('Mar', 'Mar'),
        ('Apr', 'Apr'),
        ('May', 'May'),
        ('Jun', 'Jun'),
        ('Jul', 'Jul'),
        ('Aug', 'Aug'),
        ('Sep', 'Sep'),
        ('Oct', 'Oct'),
        ('Nov', 'Nov'),
        ('Dec', 'Dec'),
    )
    label = models.CharField(max_length=20, default='reports')
    year = models.DateTimeField('date_published', auto_now=True)
    month=models.CharField(max_length=150,choices=CHOICES,default="")
    total_monthly_sales = models.IntegerField(default=0)
    total_monthly_purchases = models.IntegerField(default=0)
    total_monthly_expenses= models.IntegerField(default=0)
    employee=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="Transactionreport")

    def __str__(self):
        return self.label

    def get_absolute_url(self):
        return reverse("reports_home")
    
    
    @cached_property
    def revenue_total(self):
        method=self.total_monthly_sales-self.total_monthly_purchases
        return method
    @cached_property
    def total_income(self):
        method1=self.total_monthly_sales
        method2=self.total_monthly_expenses
        method3=self.total_monthly_purchases
        income=method1-(method2+method3)
        if income > 0:
            return "A profit of " + str(income)
        elif income == 0:
            return "A breakeven of " + str(income)
        else:
            return "A loss of " + str(abs(income))



STATUS= (
        ('pending', 'pending'),
        ('cleared', 'cleared'),
        
        
    )

class Invoice(models.Model):
    invoice_no = models.CharField(max_length=100,default="") 
    invoice_date = models.DateTimeField(default=timezone.now)
    due_date = models.CharField(max_length=100,default="") 
    your_business_name = models.CharField(max_length=100,default="") 
    customer_name = models.CharField(max_length=100,default="") 
    description = models.CharField(max_length=100,default="")
    status = models.CharField(max_length=100,choices=STATUS,default="")  
    amount_due=models.IntegerField(default=0)
    discount =models.IntegerField(default=0)
    employee=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.invoice_no

    def get_absolute_url(self):
        return reverse("invoice_home")
    
    @cached_property
    def actual_due(self):
        if self.status == "pending":
            due_amount=self.amount_due - self.discount
            return due_amount
        else:
            return 0

        

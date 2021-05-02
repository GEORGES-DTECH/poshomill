from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from django.utils.functional import cached_property
from django.db.models import Sum,Count,F
from django.utils import timezone
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta
import calendar





class Product3(models.Model):
    product=models.CharField(max_length=200,null=True,blank=True)
    quantity=models.IntegerField(default=1)
    selling_price=models.IntegerField(null=True)
    employee=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    transaction_date = models.DateTimeField(default=timezone.now)
    
    def get_absolute_url(self):
        return reverse("3product_create")
    
    def __str__(self): 
        return self.product + " @ " + '' + str(self.selling_price)
      
    

class TransactionManager(models.Manager):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.select_related('employee')
     
class Transaction3(models.Model):
   
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

    MODEEXPENSE= (
        ('Cash', 'Cash'),
        ('Mpesa', 'Mpesa'),
        ('Bank', 'Bank'),
        
    )

    STATUS= (
        ('paid', 'paid'),
        ('unpaid', 'unpaid'),
       
        
    )

    
    UNITS= (
        ('bags', 'bags'),
        ('kg', 'kg'),
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
         ('tax', 'tax'),
    )
   
    total_selling_price=models.IntegerField(null=True)
    mode_of_sale=models.CharField(choices=MODE,max_length=100,default="cash")
    purchased_products=models.CharField(max_length=100,default="")
    price_per_each= models.IntegerField(default=0)
    quantity_purchased = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    quantity_used=models.IntegerField(default=0)
    mode_of_purchase=models.CharField(choices=MODEPURCHASE,max_length=100,default="cash")
    mode_of_payment=models.CharField(choices=MODEEXPENSE,max_length=100,default="cash")
    units=models.CharField(choices=UNITS,max_length=100,default="bags")
    expense= models.IntegerField(default=0)
    amount_paid= models.IntegerField(default=0)
    customer_payment= models.IntegerField(null=True,blank=True)
    expense_description = models.CharField(choices=DESCRIPTION,max_length=100,default="")
    credit_sale_price = models.IntegerField(default=0)
    credit_purchase_price = models.IntegerField(default=0)
    customers_name = models.CharField(max_length=100,blank=True)
    suppliers_name = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=50,choices=STATUS,default="unpaid")
    transaction_date = models.DateTimeField(default=timezone.now)
    employee=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='transaction3')
    select_product1=models.ForeignKey(Product3,related_name="ts11",on_delete=models.CASCADE,null=True,blank=True)
    select_product2=models.ForeignKey(Product3,related_name="ts12",on_delete=models.CASCADE,null=True,blank=True)
    select_product3=models.ForeignKey(Product3,related_name="ts13",on_delete=models.CASCADE,null=True,blank=True)
    select_product4=models.ForeignKey(Product3,related_name="ts14",on_delete=models.CASCADE,null=True,blank=True)
    select_product5=models.ForeignKey(Product3,related_name="ts15",on_delete=models.CASCADE,null=True,blank=True)
    products_purchased = models.CharField(max_length=100, blank=True,default="")
    objects = TransactionManager()
    
    def __str__(self): 
        return self.employee
    
    def get_absolute_url(self):
        
       
        return reverse('3transaction_home')


    def get_absolute_url(self):
       
        return reverse('3transaction_home')
       
   
    @cached_property
    def change(self):
        if self.customer_payment is None:
            self.customer_payment = 0
        if self.total_selling_price is None:
            self.total_selling_price = 0
        return self.customer_payment - self.total_selling_price    
    
    @cached_property
    def total_purchases_price(self):
       total= self.quantity_purchased * self.price_per_each
       return total

    @cached_property
    def total_credit_purchase_price(self):
       total= self.quantity * self.credit_purchase_price
       return total - self.amount_paid     

    @cached_property
    def stock_quantity_left(self):
       total= self.quantity_purchased - self.quantity_used
       return total  

    @cached_property
    def stock_value_used(self):
       total= self.price_per_each * self.quantity_used
       return total               

    @cached_property
    def value_left(self):
       method = self.stock_quantity_left
       total= self.price_per_each * method
       return total               
     
    
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
        result= Transaction3.objects.filter(status="unpaid")\
            .aggregate(total=Sum('credit_sale_price'))
        return result[ 'total']

    
    
    @cached_property
    def total_credit_purchases(self):
        result= Transaction3.objects.filter(status="unpaid")\
            .aggregate(total=Sum(F('credit_purchase_price') * F('quantity')))['total']
        return result

    @cached_property
    def total_paid_amount(self):
      result= Transaction3.objects.aggregate(total=Sum('amount_paid'))
      return result[ 'total']
       
    @cached_property
    def total_creditor_balance(self):
        method1=self.total_credit_purchases
        method2 = self.total_paid_amount
        return method1 - method2
     
       

    @cached_property
    def total_purchases(self):
        result= Transaction3.objects.aggregate(total=Sum(F('quantity_purchased') * F('price_per_each')))['total']
        return result
      
    

    @cached_property
    def total_expense(self):
        result= Transaction3.objects.aggregate(total=Sum('expense'))
        return result[ 'total']
    
    @cached_property
    def total_mpesa_expense(self):
        result= Transaction3.objects.filter(mode_of_payment="Mpesa").aggregate(total=Sum('expense'))
        return result[ 'total']

      
    @cached_property
    def total_cash_expense(self):
        result= Transaction3.objects.filter(mode_of_payment="Cash").aggregate(total=Sum('expense'))
        return result[ 'total']    
    
    
    @cached_property
    def total_sales_amount(self):
      result= Transaction3.objects.aggregate(total=Sum('total_selling_price'))
      return result[ 'total']
    
    
    
    @cached_property
    def stock_value_purchased(self):
      result= Transaction3.objects.aggregate(total=Sum(F('quantity_purchased') * F('price_per_each')))['total']
      return result

    @cached_property
    def cost_of_sales(self):
       
        result= Transaction3.objects.aggregate(total=Sum(F('quantity_used') * F('price_per_each')))['total']
        return result
          
       
    
    @cached_property
    def stock_value_left(self):
        method1 = self.stock_value_purchased
        method2 = self.cost_of_sales
        return method1 - method2

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
        if self.price_per_each > 0:
            return self.price_per_each
        

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
    
      result= Transaction3.objects.filter(mode_of_sale="Mpesa")\
          .aggregate(total=Sum('total_selling_price'))
      return result[ 'total']
    
    @cached_property
    def total_cash_sales_amount(self):
    
      result= Transaction3.objects.filter(mode_of_sale="Cash")\
          .aggregate(total=Sum('total_selling_price'))
      return result[ 'total']
    
    @cached_property
    def total_bank_sales_amount(self):
    
      result= Transaction3.objects.filter(mode_of_sale="Bank")\
          .aggregate(total=Sum('total_selling_price'))
      return result[ 'total']
    

       # ===========================mpesa and cash purchase determination===========================
    @cached_property
    def total_mpesa_purchase_amount(self):
    
      result= Transaction3.objects.filter(mode_of_purchase="Mpesa").\
          aggregate(total=Sum(F('quantity_purchased') * F('price_per_each')))['total']
      return result
    
    @cached_property
    def total_cash_purchase_amount(self):
    
      result= Transaction3.objects.filter(mode_of_purchase="Cash")\
          .aggregate(total=Sum(F('quantity_purchased') * F('price_per_each')))['total']
      return result
    
    @cached_property
    def total_bank_purchase_amount(self):
    
      result= Transaction3.objects.filter(mode_of_purchase="Bank")\
          .aggregate(total=Sum(F('quantity_purchased') * F('price_per_each')))['total']
      return result
    
    @cached_property
    def mpesa_balance(self):
        method1=self.total_mpesa_sales_amount
        method2 = self.total_mpesa_purchase_amount
        method3= self.total_mpesa_expense
  
        if method1 is None:
            method1 = 0
        if method2 is None:
            method2 = 0 
        if method3 is None:
            method3 = 0          
        return method1 - (method2+method3)
    
    
    # ====================cash in hand determination===================
    @cached_property
    def total_cash_in_hand(self):
      
        method3=self.total_cash_expense
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
      result= Transaction3.objects\
          .filter(transaction_date__date=date.today()).aggregate(total=Sum('total_selling_price'))
      return result[ 'total']
    
     

    @cached_property
    def total_daily_purchases(self):
      result= Transaction3.objects\
          .filter(transaction_date__date=date.today()).aggregate(total=Sum('price_per_each'))
      return result[ 'total']
    

    @cached_property
    def total_daily_expenses(self):
      result= Transaction3.objects\
          .filter(transaction_date__date=date.today()).aggregate(total=Sum('expense'))
      return result[ 'total']
    
    @cached_property
    def total_daily_credit_sales(self):
      result= Transaction3.objects\
          .filter(transaction_date__date=date.today()).filter(status="unpaid")\
              .aggregate(total=Sum('credit_sale_price'))
      return result[ 'total']
    
    @cached_property
    def total_daily_credit_purchases(self):
      result= Transaction3.objects\
          .filter(transaction_date__date=date.today()).filter(status="unpaid")\
              .aggregate(total=Sum('credit_purchase_price'))
      return result[ 'total']
    
    
    
    
   
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
        method2 = self.cost_of_sales
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
        method2=self.cost_of_sales
        if method1 is None:
            method1 = 0
        if method2 is None:
            method2 = 0    
        return method1-method2

    @cached_property
    def profit_margin(self):
        method2 = self.cost_of_sales
        method3 = self.revenue
        difference = method3 - method2
        if difference >0: 
           return "a profit margin of "  + str(round(difference/method3 * 100,2)) + str("% was incurred")
        if difference == 0:
            return 0    
        if difference < 0:
            return "a loss of "  + str(round(difference/method3 * 100,2)) + str("% was incurred")


   
class Transactionreport3(models.Model):
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
    total_monthly_processed_goods = models.IntegerField(default=0)
    total_monthly_expenses= models.IntegerField(default=0)
    employee=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="Transactionreport3")

    def __str__(self):
        return self.label

    def get_absolute_url(self):
        return reverse("reports_home")
    
    
    @cached_property
    def revenue_total(self):
        method=self.total_monthly_sales-self.total_monthly_processed_goods
        return method
    @cached_property
    def total_income(self):
        method1=self.total_monthly_sales
        method2=self.total_monthly_expenses
        method3=self.total_monthly_processed_goods
        income=method1-(method2+method3)
        if income > 0:
            return "A profit of " + str(income)
        elif income == 0:
            return "A breakeven of " + str(income)
        else:
            return "A loss of " + str(abs(income))





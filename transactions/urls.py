from django.urls import path
from . import views
from .views import (
    TransactionHomeView,
    TransactionUpdateView,
    TransactionPurchaseUpdateView,
    TransactionDebtorView,
    TransactionCreditorView,
    
    TransactionExpenseUpdateView,
    
  
    TransactionDeleteView,
    ReportHome,
    ReportUpdateView ,
    ReportDeleteView,
    SearchResultView,
    ReportCreateView,
    DailyReportsHomeView,
    ReceiptView,
   
    IncomeHomeView,
  
    CreateProduct,
    SaleView,
    SalesdetailView,
    PurchaseView,
    ExpenseView,
    DebtorView,
    CreditorView,
    CategoryHomeView,
  
    PerformanceView,
    PaymentHomeView,
 
    ProductHomeView,
    AccountHomeView,
    UpdateProduct,
    ProductDelete,
    StaffHomeView,
    StaffDelete,
    CreateStaff,
    UpdateStaff,
    CreateProduct,
    ProductDelete,
    new_transaction,
    TransactionUpdateView,
    TransactionSearchResultView,

    
    InvoiceHomeView,
    InvoiceCreateView,
    InvoiceUpdateView,
    InvoiceDeleteView,
    InvoiceSearchResultView,
    InvoicedetailView,
    HelpView,
    PurchasedetailView,
    DebtordetailView,
    CreditordetailView,
    Branches
)


urlpatterns = [
#    =====================products urls============================
    path('products/', ProductHomeView.as_view(), name='products'),
    
    path('product/new/', CreateProduct.as_view(), name='product_create'),
   
    path('product/<int:pk>/update/', UpdateProduct.as_view(), name='product_update'),
     
     path('product/<int:pk>/delete/', ProductDelete.as_view(), name='product_delete'),
    

     # ==========================staff ulrs=====================================
   path('staffs/', StaffHomeView.as_view(), name='staffs'),
    
    path('staff/new/', CreateStaff.as_view(), name='staff_create'),
   
    path('staff/<int:pk>/update/', UpdateStaff.as_view(), name='staff_update'),
     
     path('staff/<int:pk>/delete/', StaffDelete.as_view(), name='staff_delete'),
    
#     ========================revenues urls===================================
    
    path('revenue/', IncomeHomeView.as_view(),
         name='revenue_home'),

     path('receipts/', ReceiptView.as_view(),
         name='receipts'),     
    
    path('accounts/', AccountHomeView.as_view(),
         name='accounts'),

    path('payments/', PaymentHomeView.as_view(),
         name='payments'),    
     
    path('categories/', CategoryHomeView.as_view(),
         name='category'),    
     
    path('help/', HelpView.as_view(),
         name='help'),    
     
     path('branches/', Branches.as_view(),
         name='branches'),    
     
  
    
#     ===================transactions urls==============================
    
    
    path('transaction/new/', views.new_transaction,
         name='transaction_create'),
    
    path('transaction/<int:pk>/update/',
         TransactionUpdateView.as_view(), name='transaction_update'),
     
     path('purchase/<int:pk>/update/',
         TransactionPurchaseUpdateView.as_view(), name='purchase_update'),
     
      
    path('purchase/new/', views.new_purchase,
         name='purchase_create'),
     
     path('expense/<int:pk>/update/',
         TransactionExpenseUpdateView.as_view(), name='expense_update'),
     
     path('expense/new/', views.new_expense,
         name='expense_create'),
   
     path('creditsale/<int:pk>/update/',
         TransactionDebtorView.as_view(), name='debtor_update'),
     
     path('creditsale/new/', views.new_debtor,
         name='debtor_create'),

     path('creditpurchase/<int:pk>/update/',
         TransactionCreditorView.as_view(), name='creditor_update'),
     
     path('creditpurchase/new/', views.new_creditor,
         name='creditor_create'),
     
     
     
     
     path('', TransactionHomeView.as_view(), name='transaction_home'),
     
     path('dailyreports/', DailyReportsHomeView.as_view(), name='dailyreport'),
     path('sales/', SaleView.as_view(), name='mysales'),
    path('expenses/', ExpenseView.as_view(), name='myexpenses'),
     
     path('debtors/', DebtorView.as_view(), name='mydebtors'),
     path('debtor/<int:pk>/', DebtordetailView.as_view(), name='detail_mydebtors'),
    
     
     path('creditors/', CreditorView.as_view(), name='mycreditors'),

      path('creditor/<int:pk>/', CreditordetailView.as_view(), name='detail_mycreditors'),

     
     path('purchases/', PurchaseView.as_view(), name='mypurchases'),
     path('purchase/<int:pk>/', PurchasedetailView.as_view(), name='mypurchases_detail'),

    
    
    path('performance/', PerformanceView.as_view(), name='performance'),
    
     
   
    path('transaction/<int:pk>/delete/',
         TransactionDeleteView.as_view(), name='transaction_delete'),

   
     path('sale/<int:pk>/update/',
         ReportUpdateView.as_view(), name='report_update'),
     path('sale/<int:pk>/',
         SalesdetailView.as_view(), name='sale_detail'),
    
    
#     ===================reports urls==============
    path('reports/', ReportHome.as_view(), name='reports_home'),

    path('report/new/', ReportCreateView.as_view(),
         name='report_create'),
    
    path('report/<int:pk>/delete/',
         ReportDeleteView.as_view(), name='report_delete'),

    path('sales/sale/search/',
         SearchResultView.as_view(), name='report_search'),

    path('receipt/receipts/search/',
         TransactionSearchResultView.as_view(), name='receipt_search'),
     


#  ===============invoices urls=========================
  
   path('invoices/', InvoiceHomeView.as_view(), name='invoice_home'),

    path('invoice/new/', InvoiceCreateView.as_view(),
         name='invoice_create'),


    path('invoice/<int:pk>/update/',
         InvoiceUpdateView.as_view(), name='invoice_update'),

    path('invoice/<int:pk>/delete/',
         InvoiceDeleteView.as_view(), name='invoice_delete'),

     path('invoice/<int:pk>/',
         InvoicedetailView.as_view(), name='invoice_detail'),    

    path('invoices/invoice/search/',
         InvoiceSearchResultView.as_view(), name='invoice_search'),      


    
]

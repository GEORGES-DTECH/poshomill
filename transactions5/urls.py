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
    
    ProductHomeView,
    AccountHomeView,
    UpdateProduct,
    ProductDelete,
    CreateProduct,
    ProductDelete,
    new_transaction,
    TransactionUpdateView,
    TransactionSearchResultView,
    
    PurchasedetailView,
    DebtordetailView,
    CreditordetailView,
  
    StockView,
    UpdateStock
)


urlpatterns = [
#    =====================products urls============================
    path('5products/', ProductHomeView.as_view(), name='5products'),
    
    path('5product/new/', CreateProduct.as_view(), name='5product_create'),
   
    path('5product/<int:pk>/update/', UpdateProduct.as_view(), name='5product_update'),
     
     path('5product/<int:pk>/delete/', ProductDelete.as_view(), name='5product_delete'),
    
    
#     ========================revenues urls===================================
    
    path('5revenue/', IncomeHomeView.as_view(),
         name='5revenue_home'),

     path('5receipts/', ReceiptView.as_view(),
         name='5receipts'),     
    
    path('5accounts/', AccountHomeView.as_view(),
         name='5accounts'),

   path('5stock/', StockView.as_view(),
         name='5stock'), 
  
    
#     ===================transactions urls==============================
    
    
    path('5transaction/new/', views.new_transaction,
         name='5transaction_create'),
    
    path('5transaction/<int:pk>/update/',
         TransactionUpdateView.as_view(), name='5transaction_update'),
     
     path('5purchase/<int:pk>/update/',
         TransactionPurchaseUpdateView.as_view(), name='5purchase_update'),

       path('5stock/<int:pk>/update/',
         UpdateStock.as_view(), name='5stock_update'),   
     
      
    path('5purchase/new/', views.new_purchase,
         name='5purchase_create'),
     
     path('5expense/<int:pk>/update/',
         TransactionExpenseUpdateView.as_view(), name='5expense_update'),
     
     path('5expense/new/', views.new_expense,
         name='5expense_create'),
   
     path('5creditsale/<int:pk>/update/',
         TransactionDebtorView.as_view(), name='5debtor_update'),
     
     path('5creditsale/new/', views.new_debtor,
         name='5debtor_create'),

     path('5creditpurchase/<int:pk>/update/',
         TransactionCreditorView.as_view(), name='5creditor_update'),
     
     path('5creditpurchase/new/', views.new_creditor,
         name='5creditor_create'),
     
    path('5transactions', TransactionHomeView.as_view(), name='5transaction_home'),
     
     path('5dailyreports/', DailyReportsHomeView.as_view(), name='5dailyreport'),
     path('5sales/', SaleView.as_view(), name='5mysales'),
    path('5expenses/', ExpenseView.as_view(), name='5myexpenses'),
     
     path('5debtors/', DebtorView.as_view(), name='5mydebtors'),
     path('5debtor/<int:pk>/', DebtordetailView.as_view(), name='5detail_mydebtors'),
    
     
     path('5creditors/', CreditorView.as_view(), name='5mycreditors'),

      path('5creditor/<int:pk>/', CreditordetailView.as_view(), name='5detail_mycreditors'),

     
     path('5purchases/', PurchaseView.as_view(), name='5mypurchases'),
     path('5purchase/<int:pk>/', PurchasedetailView.as_view(), name='5mypurchases_detail'),

    path('5transaction/<int:pk>/delete/',
         TransactionDeleteView.as_view(), name='5transaction_delete'),

   
     path('5sale/<int:pk>/update/',
         ReportUpdateView.as_view(), name='5report_update'),
     path('5sale/<int:pk>/',
         SalesdetailView.as_view(), name='5sale_detail'),
    
    
#     ===================reports urls==============
    path('5reports/', ReportHome.as_view(), name='5reports_home'),

    path('5report/new/', ReportCreateView.as_view(),
         name='5report_create'),
    
    path('5report/<int:pk>/delete/',
         ReportDeleteView.as_view(), name='5report_delete'),

    path('5sales/sale/search/',
         SearchResultView.as_view(), name='5report_search'),

    path('5receipt/receipts/search/',
         TransactionSearchResultView.as_view(), name='5receipt_search'),
    
    
]

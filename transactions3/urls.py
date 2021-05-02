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
    path('3products/', ProductHomeView.as_view(), name='3products'),
    
    path('3product/new/', CreateProduct.as_view(), name='3product_create'),
   
    path('3product/<int:pk>/update/', UpdateProduct.as_view(), name='3product_update'),
     
     path('3product/<int:pk>/delete/', ProductDelete.as_view(), name='3product_delete'),
    
    
#     ========================revenues urls===================================
    
    path('3revenue/', IncomeHomeView.as_view(),
         name='3revenue_home'),

     path('3receipts/', ReceiptView.as_view(),
         name='3receipts'),     
    
    path('3accounts/', AccountHomeView.as_view(),
         name='3accounts'),

   path('3stock/', StockView.as_view(),
         name='3stock'), 
  
    
#     ===================transactions urls==============================
    
    
    path('3transaction/new/', views.new_transaction,
         name='3transaction_create'),
    
    path('3transaction/<int:pk>/update/',
         TransactionUpdateView.as_view(), name='3transaction_update'),
     
     path('3purchase/<int:pk>/update/',
         TransactionPurchaseUpdateView.as_view(), name='3purchase_update'),

       path('3stock/<int:pk>/update/',
         UpdateStock.as_view(), name='3stock_update'),   
     
      
    path('3purchase/new/', views.new_purchase,
         name='3purchase_create'),
     
     path('3expense/<int:pk>/update/',
         TransactionExpenseUpdateView.as_view(), name='3expense_update'),
     
     path('3expense/new/', views.new_expense,
         name='3expense_create'),
   
     path('3creditsale/<int:pk>/update/',
         TransactionDebtorView.as_view(), name='3debtor_update'),
     
     path('3creditsale/new/', views.new_debtor,
         name='3debtor_create'),

     path('3creditpurchase/<int:pk>/update/',
         TransactionCreditorView.as_view(), name='3creditor_update'),
     
     path('3creditpurchase/new/', views.new_creditor,
         name='3creditor_create'),
     
    path('3transactions', TransactionHomeView.as_view(), name='3transaction_home'),
     
     path('3dailyreports/', DailyReportsHomeView.as_view(), name='3dailyreport'),
     path('3sales/', SaleView.as_view(), name='3mysales'),
    path('3expenses/', ExpenseView.as_view(), name='3myexpenses'),
     
     path('3debtors/', DebtorView.as_view(), name='3mydebtors'),
     path('3debtor/<int:pk>/', DebtordetailView.as_view(), name='3detail_mydebtors'),
    
     
     path('3creditors/', CreditorView.as_view(), name='3mycreditors'),

      path('3creditor/<int:pk>/', CreditordetailView.as_view(), name='3detail_mycreditors'),

     
     path('3purchases/', PurchaseView.as_view(), name='3mypurchases'),
     path('3purchase/<int:pk>/', PurchasedetailView.as_view(), name='3mypurchases_detail'),

    path('3transaction/<int:pk>/delete/',
         TransactionDeleteView.as_view(), name='3transaction_delete'),

   
     path('3sale/<int:pk>/update/',
         ReportUpdateView.as_view(), name='3report_update'),
     path('3sale/<int:pk>/',
         SalesdetailView.as_view(), name='3sale_detail'),
    
    
#     ===================reports urls==============
    path('3reports/', ReportHome.as_view(), name='3reports_home'),

    path('3report/new/', ReportCreateView.as_view(),
         name='3report_create'),
    
    path('3report/<int:pk>/delete/',
         ReportDeleteView.as_view(), name='3report_delete'),

    path('3sales/sale/search/',
         SearchResultView.as_view(), name='3report_search'),

    path('3receipt/receipts/search/',
         TransactionSearchResultView.as_view(), name='3receipt_search'),
    
    
]

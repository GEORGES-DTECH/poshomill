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
    path('4products/', ProductHomeView.as_view(), name='4products'),
    
    path('4product/new/', CreateProduct.as_view(), name='4product_create'),
   
    path('4product/<int:pk>/update/', UpdateProduct.as_view(), name='4product_update'),
     
     path('4product/<int:pk>/delete/', ProductDelete.as_view(), name='4product_delete'),
    
    
#     ========================revenues urls===================================
    
    path('4revenue/', IncomeHomeView.as_view(),
         name='4revenue_home'),

     path('4receipts/', ReceiptView.as_view(),
         name='4receipts'),     
    
    path('4accounts/', AccountHomeView.as_view(),
         name='4accounts'),

   path('4stock/', StockView.as_view(),
         name='4stock'), 
  
    
#     ===================transactions urls==============================
    
    
    path('4transaction/new/', views.new_transaction,
         name='4transaction_create'),
    
    path('4transaction/<int:pk>/update/',
         TransactionUpdateView.as_view(), name='4transaction_update'),
     
     path('4purchase/<int:pk>/update/',
         TransactionPurchaseUpdateView.as_view(), name='4purchase_update'),

       path('4stock/<int:pk>/update/',
         UpdateStock.as_view(), name='4stock_update'),   
     
      
    path('4purchase/new/', views.new_purchase,
         name='4purchase_create'),
     
     path('4expense/<int:pk>/update/',
         TransactionExpenseUpdateView.as_view(), name='4expense_update'),
     
     path('4expense/new/', views.new_expense,
         name='4expense_create'),
   
     path('4creditsale/<int:pk>/update/',
         TransactionDebtorView.as_view(), name='4debtor_update'),
     
     path('4creditsale/new/', views.new_debtor,
         name='4debtor_create'),

     path('4creditpurchase/<int:pk>/update/',
         TransactionCreditorView.as_view(), name='4creditor_update'),
     
     path('4creditpurchase/new/', views.new_creditor,
         name='4creditor_create'),
     
    path('4transactions', TransactionHomeView.as_view(), name='4transaction_home'),
     
     path('4dailyreports/', DailyReportsHomeView.as_view(), name='4dailyreport'),
     path('4sales/', SaleView.as_view(), name='4mysales'),
    path('4expenses/', ExpenseView.as_view(), name='4myexpenses'),
     
     path('4debtors/', DebtorView.as_view(), name='4mydebtors'),
     path('4debtor/<int:pk>/', DebtordetailView.as_view(), name='4detail_mydebtors'),
    
     
     path('4creditors/', CreditorView.as_view(), name='4mycreditors'),

      path('4creditor/<int:pk>/', CreditordetailView.as_view(), name='4detail_mycreditors'),

     
     path('4purchases/', PurchaseView.as_view(), name='4mypurchases'),
     path('4purchase/<int:pk>/', PurchasedetailView.as_view(), name='4mypurchases_detail'),

    path('4transaction/<int:pk>/delete/',
         TransactionDeleteView.as_view(), name='4transaction_delete'),

   
     path('4sale/<int:pk>/update/',
         ReportUpdateView.as_view(), name='4report_update'),
     path('4sale/<int:pk>/',
         SalesdetailView.as_view(), name='4sale_detail'),
    
    
#     ===================reports urls==============
    path('4reports/', ReportHome.as_view(), name='4reports_home'),

    path('4report/new/', ReportCreateView.as_view(),
         name='4report_create'),
    
    path('4report/<int:pk>/delete/',
         ReportDeleteView.as_view(), name='4report_delete'),

    path('4sales/sale/search/',
         SearchResultView.as_view(), name='4report_search'),

    path('4receipt/receipts/search/',
         TransactionSearchResultView.as_view(), name='4receipt_search'),
    
    
]

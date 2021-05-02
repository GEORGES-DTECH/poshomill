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
    path('2products/', ProductHomeView.as_view(), name='2products'),
    
    path('2product/new/', CreateProduct.as_view(), name='2product_create'),
   
    path('2product/<int:pk>/update/', UpdateProduct.as_view(), name='2product_update'),
     
     path('2product/<int:pk>/delete/', ProductDelete.as_view(), name='2product_delete'),
    
    
#     ========================revenues urls===================================
    
    path('2revenue/', IncomeHomeView.as_view(),
         name='2revenue_home'),

     path('2receipts/', ReceiptView.as_view(),
         name='2receipts'),     
    
    path('2accounts/', AccountHomeView.as_view(),
         name='2accounts'),

   path('2stock/', StockView.as_view(),
         name='2stock'), 
  
    
#     ===================transactions urls==============================
    
    
    path('2transaction/new/', views.new_transaction,
         name='2transaction_create'),
    
    path('2transaction/<int:pk>/update/',
         TransactionUpdateView.as_view(), name='2transaction_update'),
     
     path('2purchase/<int:pk>/update/',
         TransactionPurchaseUpdateView.as_view(), name='2purchase_update'),

       path('2stock/<int:pk>/update/',
         UpdateStock.as_view(), name='2stock_update'),   
     
      
    path('2purchase/new/', views.new_purchase,
         name='2purchase_create'),
     
     path('2expense/<int:pk>/update/',
         TransactionExpenseUpdateView.as_view(), name='2expense_update'),
     
     path('2expense/new/', views.new_expense,
         name='2expense_create'),
   
     path('2creditsale/<int:pk>/update/',
         TransactionDebtorView.as_view(), name='2debtor_update'),
     
     path('2creditsale/new/', views.new_debtor,
         name='2debtor_create'),

     path('2creditpurchase/<int:pk>/update/',
         TransactionCreditorView.as_view(), name='2creditor_update'),
     
     path('2creditpurchase/new/', views.new_creditor,
         name='2creditor_create'),
     
    path('2transactions2', TransactionHomeView.as_view(), name='2transaction_home'),
     
     path('2dailyreports/', DailyReportsHomeView.as_view(), name='2dailyreport'),
     path('2sales/', SaleView.as_view(), name='2mysales'),
    path('2expenses/', ExpenseView.as_view(), name='2myexpenses'),
     
     path('2debtors/', DebtorView.as_view(), name='2mydebtors'),
     path('2debtor/<int:pk>/', DebtordetailView.as_view(), name='2detail_mydebtors'),
    
     
     path('2creditors/', CreditorView.as_view(), name='2mycreditors'),

      path('2creditor/<int:pk>/', CreditordetailView.as_view(), name='2detail_mycreditors'),

     
     path('2purchases/', PurchaseView.as_view(), name='2mypurchases'),
     path('2purchase/<int:pk>/', PurchasedetailView.as_view(), name='2mypurchases_detail'),

    path('2transaction/<int:pk>/delete/',
         TransactionDeleteView.as_view(), name='2transaction_delete'),

   
     path('2sale/<int:pk>/update/',
         ReportUpdateView.as_view(), name='2report_update'),
     path('2sale/<int:pk>/',
         SalesdetailView.as_view(), name='2sale_detail'),
    
    
#     ===================reports urls==============
    path('2reports/', ReportHome.as_view(), name='2reports_home'),

    path('2report/new/', ReportCreateView.as_view(),
         name='2report_create'),
    
    path('2report/<int:pk>/delete/',
         ReportDeleteView.as_view(), name='2report_delete'),

    path('2sales/sale/search/',
         SearchResultView.as_view(), name='2report_search'),

    path('2receipt/receipts/search/',
         TransactionSearchResultView.as_view(), name='2receipt_search'),
    
    
]

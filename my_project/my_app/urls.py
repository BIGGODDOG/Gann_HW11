from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),

    # Главные списки
    path('customers/', views.customer_list, name='customer_list'),
    path('sellers/', views.seller_list, name='seller_list'),
    path('products/', views.product_list, name='product_list'),
    path('sales/', views.sale_list, name='sale_list'),
    # path('reports/', views.reports, name='reports'),
    
    # Добавление 
    path('add_customer/', views.add_customer, name='add_customer'),
    path('add_seller/', views.add_seller, name='add_seller'),
    path('add_sale/', views.add_sale, name='add_sale'),
    path('add_product/', views.add_product, name='add_product'),

    # Редактирование 
    path('customer/edit/<int:customer_id>/', views.edit_customer, name='edit_customer'),
    path('seller/edit/<int:seller_id>/', views.edit_seller, name='edit_seller'),
    path('sale/edit/<int:sale_id>/', views.edit_sale, name='edit_sale'),
    path('product/edit/<int:product_id>/', views.edit_product, name='edit_product'),

    # Удаление
    path('customer/delete/<int:customer_id>/', views.delete_customer, name='delete_customer'),
    path('seller/delete/<int:seller_id>/', views.delete_seller, name='delete_seller'),
    path('sale/delete/<int:sale_id>/', views.delete_sale, name='delete_sale'),
    path('product/delete/<int:product_id>/', views.delete_product, name='delete_product'),

    # Отчёты
    path('report/customers_of_seller/<int:seller_id>/', views.customers_of_seller, name='customers_of_seller'),
    path('report/sales_on_date/<str:sale_date>/', views.sales_on_date, name='sales_on_date'),
    path('report/sellers_of_product/<int:product_id>/', views.sellers_of_product, name='sellers_of_product'),
    path('report/customers_of_product/<int:product_id>/', views.customers_of_product, name='customers_of_product'),
    path('report/total_sales_on_date/<str:sale_date>/', views.total_sales_on_date, name='total_sales_on_date'),
    path('report/most_sold_product/', views.most_sold_product, name='most_sold_product'),
    path('report/best_seller/', views.best_seller, name='best_seller'),
    path('report/best_customer/', views.best_customer, name='best_customer'),
    # Date format YYYY-MM-DD
    path('report/most_sold_product_in_period/<str:start_date>/<str:end_date>/', views.most_sold_product_in_period, name='most_sold_product_in_period'),
    path('report/best_seller_in_period/<str:start_date>/<str:end_date>/', views.best_seller_in_period, name='best_seller_in_period'),
    path('report/best_customer_in_period/<str:start_date>/<str:end_date>/', views.best_customer_in_period, name='best_customer_in_period'),
]

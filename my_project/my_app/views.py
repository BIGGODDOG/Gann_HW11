from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer, Seller, Sale, Product
from .forms import CustomerForm, SellerForm, SaleForm, ProductForm
from django.db.models import Sum, Count
from django.utils import timezone


# Base
def base(request):
    return render(request, 'base.html')


# Главные представления 
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})

def seller_list(request):
    sellers = Seller.objects.all()
    return render(request, 'seller_list.html', {'sellers': sellers})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def sale_list(request):
    sales = Sale.objects.all()
    return render(request, 'sale_list.html', {'sales': sales})

def reports(request):
    return render(request, 'reports.html')


# Добавление
def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'add_customer.html', {'form': form})

def add_seller(request):
    if request.method == 'POST':
        form = SellerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('seller_list')
    else:
        form = SellerForm()
    return render(request, 'add_seller.html', {'form': form})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

def add_sale(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            sale = form.save(commit=False)
            sale.date = timezone.now()  
            sale.save()
            return redirect('sale_list')
    else:
        form = SaleForm()
    return render(request, 'add_sale.html', {'form': form})


# Редактирование 
def edit_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'edit_customer.html', {'form': form})

def edit_seller(request, seller_id):
    seller = get_object_or_404(Seller, id=seller_id)
    if request.method == 'POST':
        form = SellerForm(request.POST, instance=seller)
        if form.is_valid():
            form.save()
            return redirect('seller_list')
    else:
        form = SellerForm(instance=seller)
    return render(request, 'edit_seller.html', {'form': form})

def edit_sale(request, sale_id):
    sale = get_object_or_404(Sale, id=sale_id)
    if request.method == 'POST':
        form = SaleForm(request.POST, instance=sale)
        if form.is_valid():
            form.save()
            return redirect('sale_list')
    else:
        form = SaleForm(instance=sale)
    return render(request, 'edit_sale.html', {'form': form})

def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': form})


# Удаление 
def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'delete_customer.html', {'customer': customer})

def delete_seller(request, seller_id):
    seller = get_object_or_404(Seller, id=seller_id)
    if request.method == 'POST':
        seller.delete()
        return redirect('seller_list')
    return render(request, 'delete_seller.html', {'seller': seller})

def delete_sale(request, sale_id):
    sale = get_object_or_404(Sale, id=sale_id)
    if request.method == 'POST':
        sale.delete()
        return redirect('sale_list')
    return render(request, 'delete_sale.html', {'sale': sale})

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'delete_product.html', {'product': product})


# Reports
def customers_of_seller(request, seller_id):
    customers = Customer.objects.filter(sales__seller_id=seller_id).distinct()
    return render(request, 'report_customers_of_seller.html', {'customers': customers})

def sales_on_date(request, sale_date):
    sales = Sale.objects.filter(date=sale_date)
    return render(request, 'report_sales_on_date.html', {'sales': sales})

def sellers_of_product(request, product_id):
    sellers = Seller.objects.filter(sales__product_id=product_id).distinct()
    return render(request, 'report_sellers_of_product.html', {'sellers': sellers})

def customers_of_product(request, product_id):
    customers = Customer.objects.filter(sales__product_id=product_id).distinct()
    return render(request, 'report_customers_of_product.html', {'customers': customers})

def total_sales_on_date(request, sale_date):
    total_sales = Sale.objects.filter(date=sale_date).aggregate(total=Sum('amount'))['total'] or 0
    return render(request, 'report_total_sales_on_date.html', {'total_sales': total_sales})

def most_sold_product(request):
    product = Product.objects.annotate(sales_count=Count('sales')).order_by('-sales_count').first()
    return render(request, 'report_most_sold_product.html', {'product': product})

def best_seller(request):
    seller = Seller.objects.annotate(total_sales=Sum('sales__amount')).order_by('-total_sales').first()
    return render(request, 'report_best_seller.html', {'seller': seller})

def best_customer(request):
    customer = Customer.objects.annotate(total_purchases=Sum('sales__amount')).order_by('-total_purchases').first()
    return render(request, 'report_best_customer.html', {'customer': customer})

def most_sold_product_in_period(request, start_date, end_date):
    product = Product.objects.filter(sales__date__range=(start_date, end_date)).annotate(
        sales_count=Count('sales')).order_by('-sales_count').first()
    return render(request, 'report_most_sold_product_in_period.html', {'product': product})

def best_seller_in_period(request, start_date, end_date):
    seller = Seller.objects.filter(sales__date__range=(start_date, end_date)).annotate(
        total_sales=Sum('sales__amount')).order_by('-total_sales').first()
    return render(request, 'report_best_seller_in_period.html', {'seller': seller})

def best_customer_in_period(request, start_date, end_date):
    customer = Customer.objects.filter(sales__date__range=(start_date, end_date)).annotate(
        total_purchases=Sum('sales__amount')).order_by('-total_purchases').first()
    return render(request, 'report_best_customer_in_period.html', {'customer': customer})
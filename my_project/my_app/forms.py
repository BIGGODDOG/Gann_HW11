from django import forms
from .models import Customer, Seller, Product, Sale

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email']
        labels = {
            'name': 'Имя покупателя',
            'email': 'Email покупателя',
        }

class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['name', 'email', 'phone']
        labels = {
            'name': 'Имя продавца',
            'email': 'Email продавца',
            'phone': 'Телефон продавца',
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price']
        labels = {
            'name': 'Название товара',
            'price': 'Цена товара',
        }

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['customer', 'seller', 'product', 'date', 'amount']
        labels = {
            'customer': 'Покупатель',
            'seller': 'Продавец',
            'product': 'Товар',
            'date': 'Дата продажи',
            'amount': 'Сумма продажи',
        }

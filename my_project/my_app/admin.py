from django.contrib import admin
from my_app.models import Customer, Seller, Sale, Product

# Register your models here.

admin.site.register(Customer)
admin.site.register(Seller)
admin.site.register(Sale)
admin.site.register(Product)
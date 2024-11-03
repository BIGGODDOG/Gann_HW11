from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя покупателя")
    email = models.EmailField(verbose_name="Email покупателя")

    def __str__(self):
        return self.name


class Seller(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя продавца")
    email = models.EmailField(verbose_name="Email продавца")
    phone = models.CharField(max_length=20, verbose_name="Телефон продавца", blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название товара")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена товара")

    def __str__(self):
        return self.name


class Sale(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="sales", verbose_name="Покупатель")
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name="sales", verbose_name="Продавец")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="sales", verbose_name="Товар")
    date = models.DateField(verbose_name="Дата продажи")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма продажи")

    def __str__(self):
        return f"Продажа {self.product} покупателю {self.customer} от {self.date}"
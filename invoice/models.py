from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    address = models.CharField(max_length=100, blank=True, default='')
    phone = models.CharField(max_length=100, blank=True, default='')

""" 


class Product(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    price = models.IntegerField()


class Invoice(models.Model):
    customer_id = models.ForeignKey(Customer)
    discount = models.IntegerField()
    total = models.IntegerField()


class InvoiceItem(models.Model):
    invoice_id =  models.ForeignKey(Invoice)
    product_id =  models.ForeignKey(Product)
    quantity = models.IntegerField()

"""
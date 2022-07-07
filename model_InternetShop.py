from django.db import models

director = 'DI'
admin = 'AD'
cook = 'CO'
cashier = 'CA'
cleaner = 'CL'

POSITIONS = [
    (director, 'Директор'),
    (admin, 'Администратор'),
    (cook, 'Повар'),
    (cashier, 'Кассир'),
    (cleaner, 'Уборщик')
]

class Product(models.Model):
    name = models.CharField(max_lenght = 255)
    price = models.FloatField(default = 0.0)
    composition = models.TextField(default = "Состав не указан")


class Staff(models.Model):
    full_name = CharField(max_lenght = 255)
    labor_contract = IntegerField()
    position = CharField(max_lenght = 2,
                            choices = POSITIONS,
                            default = cashier)

class Order(models.Model):
    time_in = models.DateTimeField(auto_now_add = True)
    time_out = models.DateTimeField(null = True)
    cost = models.FloatField(default = 0.0)
    pickup = models.BooleanField(default = False)
    complete = models.BooleanField(default = False)
    staff = models.ForeignKey(Staff, on_delete = models.CASCADE)

    products = models.ManyToManyField(Product, through = 'ProductOrder')

class ProductOrder(models.Model):
    product = models.ForeignKey(Products, on_delete = models.CASCADE)
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
    amount =IntegerField(default = 1)





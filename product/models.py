from django.db import models
from user.models import UserModel
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    name = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    stock = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Orderstatus(models.Model):
    order = [
        ('주문 완료','주문 완료'),
        ('결제 완료','결제완료'),
        ('취소','취소'),
        ('배송출발','배송출발'),
        ('배송완료','배송완료'),
    ]
    field = models.CharField(max_length=10, choices=order)


class ProductOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='products')
    product_count = models.PositiveIntegerField()


class UserOrder(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True, related_name='User')
    productorder = models.ManyToManyField(ProductOrder,related_name='followee')
    orderstate = models.ForeignKey(Orderstatus, on_delete=models.SET_NULL, null=True, related_name='Order_status')
    delivery_adress = models.CharField(max_length=200, db_index=True)
    Ordertime = models.DateTimeField(auto_now_add=True)
    totalprice = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    finalprice = models.DecimalField(max_digits=10, decimal_places=2)










import datetime

from django.shortcuts import render, get_object_or_404
from .models import (
    Category,
    Product,
    ProductOrder,
    OrderStatus,
    UserOrder
)
from user.models import User
from django.db import transaction


def categorize_product(request, category_name=None, id=None):
    if request.method == 'GET':
        categories = Category.objects.all()
        products = Product.objects.all()

        return render(request, 'list.html', {'categories': categories, 'products': products})


def product_detail(request, id, product_name):
    product = get_object_or_404(Product, id=id, name=product_name)

    return render(request, 'detail.html', {'product': product})


INITIAL_ORDER_STATUS = 1


@transaction.atomic
def product_order(request):
    product = request.POST.get("product")
    quantity = request.POST.get('quantity')
    address = request.POST.get('address')
    print(product,'1', quantity,'1', address)

    item = Product.objects.get(name=product)

    # 주문한 유저
    user = User.objects.get(id=1)  # 인증 생략 하드코딩

    order_stats = OrderStatus.objects.get(status_name='order placed')

    product_order = ProductOrder.objects.create(product=item, product_count=quantity)

    final_price = ((item.price * quantity) * 1)

    user_order = UserOrder(
        user=user,
        product_order=product_order,
        order_status=order_stats,
        delivery_address=address,
        order_time=datetime.datetime.now(),
        total_price=item.price * quantity,
        discount=1,
        final_price=final_price,
        active=True
    )

    user_order.save()

    product_order.user_order = user_order
    product_order.save()

    return render(request, 'complete.html')

from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from order.models import Order, OrderDetail
from shop.models import ProductList


def add_product(request: HttpRequest):
    product_id = request.GET.get('product_id')
    count = request.GET.get('count')
    if request.user.is_authenticated:
        product = ProductList.objects.filter(id=product_id, is_delete=False, is_active=True).first()
        if product is not None:
            user_order, created = Order.objects.get_or_create(is_order_paid=False, user_id=request.user.id)
            user_order_detail = user_order.orderdetail_set.filter(product_id=product_id).first()
            if user_order_detail is not None:
                user_order_detail.count += int(count)
                user_order_detail.save()
                return JsonResponse({
                    'status': 'success'
                })
            else:
                new_order_detail = OrderDetail(order_id=user_order.id, product_id=product_id, count=count)
                new_order_detail.save()
        else:

            return JsonResponse({
                'status': 'product_not_found'
            })
    else:
        return JsonResponse({
            'status': 'not_login'
        })

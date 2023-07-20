from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView
from dashbord.forms import EditProfileForms, DiscountForm
from order.models import Order, OrderDetail
from shop.models import Discount


@method_decorator(login_required, 'dispatch')
class Dashbord(TemplateView):
    template_name = 'dashbord/dashbord.html'


@method_decorator(login_required, 'dispatch')
class EditProfile(View):
    def get(self, request):
        editprofile = EditProfileForms()
        context = {
            'form': editprofile,
        }
        return render(request, 'dashbord/edit_profile.html', context)

    def post(self, request: HttpRequest):
        pass


@login_required
def dashbord_component(request):
    return render(request, 'dashbord/component/dashbord_component.html')


@login_required
def user_cart(request: HttpRequest):
    user_order, create = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_order_paid=False,
                                                                                         user_id=request.user.id)
    total = user_order.total_price()
    form = DiscountForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user_discount_code = form.cleaned_data["code"]
            find_discount_code = Discount.objects.filter(discount_code=user_discount_code).exists()
            if find_discount_code:
                discount_code = Discount.objects.filter(discount_code=user_discount_code).first()
                discount_value = discount_code.discount_value
                total -= discount_value
    context = {
        'order': user_order,
        'total': total,
        'discount_form': form,
    }
    return render(request, 'dashbord/user_cart.html', context)


def delete_from_order_items(request: HttpRequest):
    item_id = request.GET.get('detail_id')
    if item_id is None:
        return JsonResponse({
            'status': 'item-id-not-found'
        })
    del_number, del_item = OrderDetail.objects.filter(id=item_id, order__is_order_paid=False,
                                                      order__user_id=request.user.id).delete()
    if del_number == 0:
        return JsonResponse({
            'status': 'item-not-found'
        })
    user_order, create = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_order_paid=False,
                                                                                         user_id=request.user.id)
    total = user_order.total_price()
    context = {
        'order': user_order,
        'total': total
    }
    html_component = render_to_string('dashbord/component/user_cart_component.html', context)
    return JsonResponse({
        'status': 'success',
        'data': html_component
    })


def cheng_item_count(request: HttpRequest):
    item_id = request.GET.get('detail_id')
    position = request.GET.get('position')
    if item_id is None or position is None:
        return JsonResponse({
            'status': 'item_position_not_found'
        })
    item = Order.objects.filter(id=item_id, order__user_id=request.user.id, order__is_order_paid=False).first()
    if item is None:
        return JsonResponse({
            'status': 'item_not_found'
        })
    if position == 'increase':
        item.count += 1
        item.save()
    elif position == 'decrease':
        item.count -= 1
        item.save()
    else:
        return JsonResponse({
            'status': 'invalid_count'
        })

    user_order, create = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_order_paid=False,
                                                                                         user_id=request.user.id)
    total = user_order.total_price()
    context = {
        'order': user_order,
        'total': total
    }
    html_component = render_to_string('dashbord/component/user_cart_component.html', context)
    return JsonResponse({
        'status': 'success',
        'data': html_component
    })

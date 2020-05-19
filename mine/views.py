from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Sum, Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views.generic import DetailView, ListView

from mall.models import Product
from mine.models import Order, Cart
from utils import constants, tools


class OrderDetailView(DetailView):
    model = Order
    slug_field = 'sn'
    slug_url_kwarg = 'sn'
    template_name = 'order_info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['constants'] = constants
        return context

@login_required
@transaction.atomic()
def cart_add(request, prod_uid):
    user = request.user
    product = get_object_or_404(Product, uid=prod_uid, is_valid=True, status=constants.PRODUCT_STATUS_SELL)
    count = int(request.POST.get('count', 1))
    if product.remain_count < count:
        return HttpResponse('no')
    product.update_store_count(count)
    try:
        cart = Cart.objects.get(product=product, user=user, status=constants.ORDER_STATUS_INIT)
        count = cart.count + count
        cart.count = count
        cart.amount = count * cart.price
    except Cart.DoesNotExist:
        Cart.objects.create(product=product,
                            user=user,
                            name=product.name,
                            img=product.img,
                            price=product.price,
                            origin_price=product.origin_price,
                            count=count,
                            amount=count*product.price)
    return HttpResponse('ok')

@login_required
def cart(request):
    user = request.user
    prod_list = user.carts.filter(status=constants.ORDER_STATUS_INIT)
    if request.method == 'POST':
        default_addr = user.default_addr
        if not default_addr:
            messages.warning(request, '请选择地址信息')
            return redirect('accounts:address_list')
        cart_total = prod_list.aggregate(sum_amount=Sum('amount'), sum_count=Sum('count'))
        order = Order.objects.create(
            user=user,
            sn=tools.gen_trans_id(),
            buy_amount=cart_total['sum_amount'],
            buy_count=cart_total['sum_count'],
            to_user=default_addr.username,
            to_area=default_addr.get_region_format(),
            to_address=default_addr.address,
            to_phone=default_addr.phone,
        )
        prod_list.update(status=constants.ORDER_STATUS_SUBMIT, order=order)
        messages.success(request, '下单成功，请支付！')
        return redirect('mine:order_detail', order.sn)
    return render(request, 'cart.html', {
        'prod_list': prod_list
    })

@login_required
def order_pay(request):
    user = request.user
    if request.method == 'POST':
        sn = request.POST.get('sn', None)
        order = get_object_or_404(Order, sn=sn, user=user, status=constants.ORDER_STATUS_SUBMIT)
        if order.buy_amount > user.integral:
            messages.error(request, '积分余额不足')
            return redirect('mine:order_detail', sn=sn)
        user.ope_integral_account(0, order.buy_amount)
        order.status = constants.ORDER_STATUS_PAIED
        order.save()
        order.carts.all().update(status=constants.ORDER_STATUS_PAIED)
        messages.success(request, '支付成功')
    return redirect('mine:order_detail', sn=sn)


@login_required
def index(request):
    return  render(request, 'mine.html', {
        'constants': constants
    })


# @login_required
# def order_list(request):
#     status = request.GET.get('status')
#     if status:
#         status = int(status)
#     return render(request, 'all_orders.html', {
#         'constants': constants,
#         'status': status
#     })

class OrderListView(ListView):
    model = Order
    template_name = 'all_orders.html'

    def get_queryset(self):
        status = self.request.GET.get('status', '')
        if status:
            status = int(status)
        user = self.request.user
        query = Q(user=user)
        if status:
            query = query & Q(status=status)
        return Order.objects.filter(query).exclude(
            status=constants.ORDER_STATUS_DELETE
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        status = self.request.GET.get('status', '')
        if status:
            status = int(status)
        context['status'] = status
        context['constants'] = constants
        return context

@login_required
def prod_collect(request):
    return render(request, 'shoucang.html', {})
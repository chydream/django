from django.db.models import Q
from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.views.generic import ListView

from mall.models import Product
from utils import constants


def pro_list(request):
    prod_list = Product.objects.filter(status=constants.PRODUCT_STATUS_SELL,is_valid=True)
    name = request.GET.get('name', '')
    if name:
        pro_list = prod_list.filter(name__icontains=name)
    return render(request, 'pro_list.html',{
        'prod_list': prod_list
    })

def pro_info(request, pk):
    prod_obj = get_object_or_404(Product, uid=pk, is_valid=True)
    return render(request, 'pro_info.html', {
        'prod_obj': prod_obj
    })


class ProductList(ListView):
    paginate_by = 6
    template_name = 'pro_list.html'
    def get_queryset(self):
        query = Q(status=constants.PRODUCT_STATUS_SELL, is_valid=True)
        name = self.request.GET.get('name', '')
        if name:
           query = query & Q(name__icontains=name)

        tag = self.request.GET.get('tag', '')
        if tag:
            query = query & Q(tags__code=tag)
        return Product.objects.filter(query)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['search_name'] = self.request.GET.get('name', '')
        context['search_data'] = self.request.GET.dict()
        return context

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from weibo.models import WeiboUser


def page_user(request, page):
    page_size = 10
    user_list = WeiboUser.objects.all()
    p = Paginator(user_list, page_size)
    print(p.count)
    print(p.num_pages)
    try:
        page_data = p.page(page)
        print(page_data.object_list)
    except PageNotAnInteger as e:
        print('页码错误')
    except EmptyPage as e:
        print('没有数据了')
    return HttpResponse('ok')
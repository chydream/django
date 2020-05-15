import math
import os
from datetime import datetime

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, FileResponse
from django.shortcuts import render_to_response, render, redirect
from django.template import loader
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from django.views.generic import TemplateView

from accounts.models import User
from system.models import Slider, News
from utils import constants


def index(request):
    # url = reverse("article_detail", args=(2020,))
    # url_auth = reverse('auth:index')
    # print(url_auth)
    # return HttpResponse("ok:"+url)
    slider_list = Slider.objects.filter(types=constants.SLIDER_TYPE_INDEX)
    now_time = datetime.now()
    news_list = News.objects.filter(types=constants.NEWS_TYPE_NEW,
                                    is_top=True,
                                    is_valid=True,
                                    start_time__lte=now_time,
                                    end_time__gte=now_time)
    # user_id = request.session[constants.LOGIN_SESSION_ID]
    # user = User.objects.get(pk=user_id)
    return render(request, 'index.html', {
        'slider_list': slider_list,
        'news_list': news_list,
        # 'user': user
    })


def index_one(request):
    # url = reverse('index_two')
    # print(url)
    # return HttpResponseRedirect(url)
    return redirect('index_two')
    # return HttpResponse("index one")

def index_two(request):
    return HttpResponse("index two")


def article(request, year):
    params = request.GET.get('day', None)
    curent_now = datetime.now()

    # raise ValueError
    raise PermissionDenied


    # html = """
    # <html>
    #     <head>
    #         <style type="text/css">
    #             body{{color:#000}}
    #         </style>
    #     </head>
    #     <body>
    #         <p>now:{0}</p>
    #         <p>{1}<p>
    #     </body>
    # </html>
    # """.format(curent_now, params)
    html = ''
    # return HttpResponse("article:" + year + '<br/>' + html)


    # 方法1
    # path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\templates\\test.html'
    # file = open(path, 'r', encoding='utf-8')
    # html = file.read()
    # html = html.replace('{{0}}', str(curent_now))
    # html = html.replace('{{1}}', params)
    # print(curent_now)
    # print(params)
    # file.close()
    # return HttpResponse(html)

    # 方法2
    # return render(request, 'test.html', {
    #     "now": curent_now
    # })

    #方法3
    # return render_to_response('test.html', {
    #     "now": curent_now
    # })

    #方法4
    # temp = loader.get_template('test.html')
    # html = temp.render({
    #     "now": curent_now
    # })
    # return HttpResponse(html)

def page_500(request):
    return HttpResponse("服务器正忙")

def page_404(request):
    return HttpResponse("404报错")

def print_request(request):
    print(request.META['REMOTE_ADDR'])
    print(request.META['HTTP_USER_AGENT'])
    print(request.COOKIES)
    print(request.FILES)
    print(dir(request.session))
    print('-----------------')
    print(dir(request))
    return HttpResponse()



# text/html  text/plain  text/xml  image/png  image/jpeg  image/gif   application/json
def print_res(request):
    temp = loader.get_template('test.html')
    html = temp.render({
        "now": datetime.now()
    })
    return HttpResponse(html, content_type='text/plain')

def print_json(request):
    user_info = {
        'username': '张三',
        'age': 13
    }
    return JsonResponse(user_info, content_type='application/json')

    # import json
    # user_info = json.dumps(user_info)
    # return HttpResponse(user_info, content_type='application/json')

def print_attr(request):
    res = HttpResponse('打印相应状态码', status=201)
    # print(res.status_code)
    # res.write('2019')
    return res

def print_image(request):
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\medias\\images\\1.jpg'
    f = open(path, 'rb')
    return FileResponse(f, content_type='image/jpeg')

def print_excel(request):
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\medias\\excel\\1.xls'
    f = open(path, 'rb')
    return FileResponse(f, content_type='application/vnd.ms-excel')

def templ_show(request):
    lsit_city = ('长沙', '广州', '深圳')
    list_prods = [
        {'name': '名称1', 'price': 101},
        {'name': '名称2', 'price': 102},
        {'name': '名称3', 'price': 103}
    ]
    user_info = {
        'name': '名称1',
        'age': 20
    }
    list_empty = []
    return render(request, 'detail.html', {
        'username': 'chy',
        'list_city': lsit_city,
        'list_prods': list_prods,
        'list_empty': list_empty,
        'user_info': user_info,
        'name': 'chy',
        'now': datetime.now(),
        'pi': math.pi,
        'html': '<h1>我是主标题，大家好</h1>',
        'money': 300055.33
    })

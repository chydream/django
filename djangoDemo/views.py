import os
from datetime import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render, redirect
from django.template import loader
from django.urls import reverse


def index(request):
    # url = reverse("article_detail", args=(2020,))
    # url_auth = reverse('auth:index')
    # print(url_auth)
    # return HttpResponse("ok:"+url)
    return render_to_response('index.html')


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

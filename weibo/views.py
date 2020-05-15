import os

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import transaction, connection
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
import mysql.connector.pooling

# Create your views here.
from djangoDemo import settings
from utils.sqlpage import SqlPaginator
from weibo.forms import LoginForm, UserLoginForm, UserRegistForm, UserForm, AvatarUploadForm, WeiboImageForm
from weibo.models import WeiboUser, Weibo, Comment


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


@transaction.atomic()  #事务 自动提交回滚
def page_trans(request):
    user = WeiboUser.objects.get(pk=1)
    weibo = Weibo.objects.create(user=user, content='事务练习')
    comment = Comment.objects.create(user=user, content='微博评论', weibo=weibo)
    print('weibo:', weibo.pk, ';comment:' ,comment.id)
    return HttpResponse('OK')


def page_trans_with(request):
    with transaction.atomic():
        user = WeiboUser.objects.get(pk=1)
        weibo = Weibo.objects.create(user=user, content='事务练习with')
        comment = Comment.objects.create(user=user, content='微博评论with', weibo=weibo)
        print('weibo:', weibo.pk, ';comment:', comment.id)
    return HttpResponse('ok')


def page_trans_hand(request):
    try:
        transaction.set_autocommit(False) #默认自动提交，放弃自动提交
        user = WeiboUser.objects.get(pk=1)
        print(user.query)
        weibo = Weibo.objects.create(user=user, content='事务练习with')
        comment = Comment.objects.create(user=user, content='微博评论with', weibo=weibo)
        print('weibo:', weibo.pk, ';comment:', comment.id)
        transaction.commit()
    except Exception as e:
        # weibo.delete()
        print(e)
        transaction.rollback()
    return HttpResponse('ok')


def page_q(request):
    # user_list = WeiboUser.objects.filter(username='张三')
    # user_list2 = WeiboUser.objects.filter(nickname='张三')
    query = Q(username='zhangsan') | Q(nickname='张三')  # | & !
    query2 = Q(username='zhangsan') & Q(nickname='张三')
    user_list = WeiboUser.objects.filter(query2)
    print(user_list)
    return HttpResponse('ok')

def page_sql(request):
    cursor = connection.cursor()
    username = '张三'
    sql = 'SELECT id, username, nickname FROM  weibo_user ' \
          'WHERE username = %s '
    cursor.execute(sql, (username,))
    result = cursor.fetchone()
    print(123)
    print(result)
    # user_list = WeiboUser.objects.raw(sql, (username,))
    # for item in user_list:
    #     print(item)
    return HttpResponse('ok')


def page_sql2(request):
    sql = 'SELECT id, username, nickname FROM  weibo_user '
    params = []
    page_size = 10
    sqlpg = SqlPaginator(sql, params, page_size)
    result = sqlpg.page(1)
    # for item in result:
    #     print(item)
    count_num = sqlpg.count()
    print(count_num)
    print(sqlpg.total())
    return HttpResponse('ok')


def page_comments(request):
    comments_list = Comment.objects.all().select_related('weibo','user')
    return render(request, 'comments.html', {
        'comments_list':comments_list
    })


def page_form_first(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        # print(form.is_bound)
        if form.is_valid():
            data = form.cleaned_data
            print(data['username'])
    else:
        form = LoginForm(initial={'username': '你好'})
        form = form.as_p()
        # print(form.is_bound)
        # errors fields initial
    return render(request, 'page_form_first.html', {
        'form': form
    })


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
        else:
            print(form.errors)
    else:
        form = UserLoginForm()
    return  render(request, 'user_login.html', {
        'form': form
    })


def user_register(request):
    form = UserRegistForm()
    return  render(request, 'user_register.html', {
        'form': form
    })


def user_edit(request):
    form = UserForm()
    return render(request, 'user_edit.html', {
        'form':form
    })


def user_edit(request):
    form = UserForm()
    return render(request, 'user_edit.html', {
        'form': form
    })


def file_upload_origin(request):
    if request.method == 'POST':
        fileData = request.FILES.get('avatar', None)
        filepath = os.path.join(settings.MEDIA_ROOT, 'images', str(fileData))
        print(filepath)
        f = open(filepath, 'wb+')
        for chunk in fileData.chunks():
            f.write(chunk)
        f.close()
        # print(fileData)
    return render(request, 'file_upload_origin.html', {

    })

def file_upload_form(request):
    if request.method == 'POST':
        form = AvatarUploadForm(request.POST, request.FILES)
        if form.is_valid():
            fileData = request.FILES.get('avatar', None)
            filepath = os.path.join(settings.MEDIA_ROOT, 'images', str(fileData))
            f = open(filepath, 'wb+')
            for chunk in fileData.chunks():
                f.write(chunk)
            print('上传成功')
            f.close()
    else:
        form = AvatarUploadForm()
    return render(request, 'file_upload_form.html', {
        'form': form
    })


def file_upload_weibo(request):
    user = WeiboUser.objects.get(pk =1 )
    if request.method == 'POST':
        form = WeiboImageForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(user, False)
            # print(obj.pk)
    else:
        form = WeiboImageForm()
    return render(request, 'file_upload_weibo.html',{
        'form': form
    })
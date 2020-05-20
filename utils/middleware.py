from django.http import HttpResponse

from accounts.models import User


def ip_middleware(get_response):

    def middleware(request):
        print('请求到达前的业务逻辑')
        ip = request.META.get('REMOTE_ADDR', None)
        ip_disable_list = [
            '127.0.0.1'
        ]
        print(ip)
        if ip in ip_disable_list:
            return HttpResponse('not allowed', status=403)
        response = get_response(request)
        print('在视图函数调用之后的业务逻辑')
        return response

    return middleware



class MallAuthMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        print('MallAuthMiddleware请求到达前的业务逻辑')
        user_id = request.session.get('user_id', None)
        if user_id:
            user = User.objects.get(pk=user_id)
        else:
            user = None

        request.my_user = user

        response = self.get_response(request)


        print('MallAuthMiddleware在视图函数调用之后的业务逻辑')
        return response
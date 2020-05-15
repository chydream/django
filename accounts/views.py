from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from accounts.forms import UserLoginForm, UserRegistForm, UserAddressForm
from accounts.models import User, UserAddress
from utils import constants
from utils.verify import VerifyCode


def user_login(request):
    next_url = request.GET.get('next', 'index')
    if request.method == 'POST':
        form = UserLoginForm(request=request, data=request.POST)
        code = request.POST.get('verify_code', None)
        client =VerifyCode(request)
        rest = client.validate_code(code)
        if form.is_valid():
            data = form.cleaned_data
            # user = User.objects.get(username=data['username'], password=data['password'])
            # request.session[constants.LOGIN_SESSION_ID] = user.id
            # return redirect('index')
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                return redirect(next_url)
        else:
            print(form.errors)
    else:
        form = UserLoginForm(request)
    return render(request, 'login.html', {
        'form': form,
        'next_url': next_url
    })

def user_logout(request):
    logout(request)
    return redirect('index')

def user_register(request):
    if request.method == 'POST':
        form = UserRegistForm(request=request, data=request.POST)
        print(456)
        if form.is_valid():
            form.register()
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = UserRegistForm(request)
    return render(request, 'regist.html', {
        'form': form
    })

@login_required
def address_list(request):
    my_addr_list = UserAddress.objects.filter(user=request.user, is_valid=True)
    return render(request, 'address_list.html', {
        'my_addr_list': my_addr_list
    })

@login_required
def address_edit(request, pk):
    # print(pk)
    user = request.user
    addr = None
    initial = {}
    if pk.isdigit():
        addr = get_object_or_404(UserAddress, pk=pk, user=user, is_valid=True)
        initial['region'] = addr.get_region_format()
    if request.method == 'POST':
        form = UserAddressForm(request=request, data=request.POST,instance=addr,initial=initial)
        if form.is_valid():
            form.save()
            return redirect('accounts:address_list')
    else:
        form = UserAddressForm(request=request, instance=addr,initial=initial)
    return render(request, 'address_edit.html', {
        'form': form
    })

@login_required
def address_delete(request, pk):
    addr = get_object_or_404(UserAddress, pk=pk, is_valid=True, user=request.user)
    addr.is_valid = False
    addr.save()
    return HttpResponse('ok')

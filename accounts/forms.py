import re

from django import forms
from django.contrib.auth import authenticate, login

from accounts.models import User, UserAddress
# from django.contrib.auth.models import User

from utils.verify import VerifyCode
from weibo.models import WeiboUser, WeiboImage, Weibo


class LoginForm(forms.Form):
    SEX_CHOICES = (
        (1,'男'),
        (0,'女'),
    )
    username = forms.CharField(label='用户名', max_length=64, required=False)
    email = forms.EmailField(label='电子邮件')
    sex = forms.ChoiceField(label='性别', choices=SEX_CHOICES)
    birth = forms.DateField(label='生日')
    remark = forms.CharField(label='备注', max_length=200, widget=forms.Textarea)
    # initial='什么', widget='textarea', help_text='使用帮助',error_messages='errors', localize=True, disabled=True


class UserLoginForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=64, error_messages={
        'required': '请输入用户名',

    })
    password = forms.CharField(label='密码', max_length=64, widget=forms.PasswordInput, error_messages={
        'required': '请输入密码',

    })
    verify_code = forms.CharField(label='验证码', max_length=4, error_messages={
        'required': '请输入验证码'
    })

    def __init__(self, request,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     pattern = r'0{0,1}1[0-9]{10}$'
    #     if not re.search(pattern, username):
    #         raise forms.ValidationError('请输入正确的手机号码')
    #     return username

    def clean_verify_code(self):
        verify_code = self.cleaned_data['verify_code']

        if not verify_code:
            raise forms.ValidationError('请输入验证码')
        client = VerifyCode(self.request)
        if not client.validate_code(verify_code):
            raise forms.ValidationError('您输入的验证码不正确')
        return verify_code

    def clean(self):
        clearned_data = super().clean()
        username = clearned_data.get('username', None)
        password = clearned_data.get('password', None)
        print(username,password)
        if username and password:
            user_list = User.objects.filter(username = username)
            if user_list.count() == 0:
                raise forms.ValidationError('用户名不匹配')
            # print(user_list.filter(password = password).exists())
            # if not user_list.filter(password = password).exists():
            #     raise forms.ValidationError('密码不匹配')
            if not authenticate(username=username, password=password):
                raise forms.ValidationError('密码不匹配')
        # username = clearned_data['username']
        return clearned_data


class UserRegistForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=64)
    nickname = forms.CharField(label='昵称', max_length=64)
    password = forms.CharField(label='设置密码', max_length=64, widget=forms.PasswordInput)
    password_repeat = forms.CharField(label='确认密码', max_length=64, widget=forms.PasswordInput)
    verify_code = forms.CharField(label='验证码', max_length=4)

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request


    def clean_username(self):
        username = self.cleaned_data.get('username', None)
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('用户名存在')
        return username


    def clean_verify_code(self):
        verify_code = self.cleaned_data['verify_code']

        if not verify_code:
            raise forms.ValidationError('请输入验证码')
        client = VerifyCode(self.request)
        if not client.validate_code(verify_code):
            raise forms.ValidationError('您输入的验证码不正确')
        return verify_code

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password', None)
        password_repeat = cleaned_data.get('password_repeat', None)
        if password and password_repeat:
            if password != password_repeat:
                raise  forms.ValidationError('两次密码输入不一致')
        return cleaned_data

    def register(self):
        data = self.cleaned_data
        print(data['username'], data['password'])
        User.objects.create_user(username=data['username'], password=data['password'], nickname=data['nickname'], level=0)
        user = authenticate(username=data['username'], password=data['password'])
        login(self.request, user)
        return user

class UserForm(forms.ModelForm):
    class Meta:
        model = WeiboUser
        fields = ['username', 'password', 'nickname']
        widgets = {
            'password': forms.PasswordInput(attrs={
                'class': 'text-error'
            })
        }
        labels = {
            'username': '手机号码'
        }
        error_messages = {
            'username': {
                'required': '请输入手机号码',
                'max_length': '最大长度不超过32位'
            }
        }

class AvatarUploadForm(forms.Form):
    remark = forms.CharField(label='备注', max_length=32)
    avatar = forms.ImageField(label='头像')

class WeiboImageForm(forms.ModelForm):
    content = forms.CharField(label='内容', max_length=256, widget=forms.Textarea(attrs={
        'placeholder': '请输入内容'
    }))
    class Meta:
        model = WeiboImage
        fields = ['image']

    def save(self, user, commit=False):
        obj = super().save(commit)
        data = self.cleaned_data
        content = data['content']
        weibo = Weibo.objects.create(user=user, content=content)
        obj.weibo = weibo
        obj.save()
        return obj


class UserAddressForm(forms.ModelForm):
    region = forms.CharField(label='大区域选项', max_length=64, required=True, error_messages={
        'required': '请选择地址'
    })
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    class Meta:
        model = UserAddress
        fields = ['address', 'username', 'phone', 'is_default']
        widgets={
            'is_default':forms.CheckboxInput(attrs={
                'class': 'weui-switch'
            })
        }


    def clean_phone(self):
        phone = self.cleaned_data['phone']
        pattern = r'0{0,1}1[0-9]{10}$'
        if not re.search(pattern, phone):
            raise forms.ValidationError('请输入正确的手机号码')
        return phone

    def clean(self):
        cleaned_data = super().clean()
        addr_list = UserAddress.objects.filter(is_valid=True, user=self.request.user)
        if addr_list.count() >= 20:
            raise forms.ValidationError('最多只能添加20个地址')
        return cleaned_data

    def save(self,commit=True):
        obj = super().save(commit=False)
        region = self.cleaned_data['region']
        (province, city, area) = region.split(' ')
        obj.province = province
        obj.city = city
        obj.area = area
        obj.user = self.request.user
        if self.cleaned_data['is_default']:
            UserAddress.objects.filter(is_valid=True, user=self.request.user, is_default=True).update(is_default=False)
        obj.save()
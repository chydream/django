import re

from django import forms

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
    username = forms.CharField(label='用户名', max_length=64)
    password = forms.CharField(label='密码', max_length=64, widget=forms.PasswordInput)
    verify_code = forms.CharField(label='验证码', max_length=4)
    def clean_username(self):
        username = self.cleaned_data['username']
        pattern = r'0{0,1}1[0-9]{10}$'
        if not re.search(pattern, username):
            raise forms.ValidationError('请输入正确的手机号码')
        return username

    def clean(self):
        clearned_data = super().clean()
        username = clearned_data.get('username', None)
        password = clearned_data.get('password', None)
        print(username,password)
        if username and password:
            user_list = WeiboUser.objects.filter(username = username)
            if user_list.count() == 0:
                raise forms.ValidationError('用户名不匹配')
            print(user_list.filter(password = password).exists())
            if not user_list.filter(password = password).exists():
                raise forms.ValidationError('密码不匹配')
        # username = clearned_data['username']
        return clearned_data


class UserRegistForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=64)
    nickname = forms.CharField(label='昵称', max_length=64)
    password = forms.CharField(label='设置密码', max_length=64, widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='确认密码', max_length=64, widget=forms.PasswordInput)
    verify_code = forms.CharField(label='验证码', max_length=4)

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
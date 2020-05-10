from django.db import models

from django.contrib.auth.models import User

class MyUser(User):
    class Meta:
        proxy = True

    def get_format_username(self):
        return self.username[:3]+'***'



class UserManager(models.Manager):
    def top_users(self):
        return self.all().order_by('-crated_at')[:5]
        # return []



# Create your models here.
class WeiboUser(models.Model):
    USER_STATUS = (
        (2, '限制用户'),
        (1, '正常'),
        (0, '删除')
    )
    username = models.CharField('用户名', max_length=32)
    password = models.CharField('密码', max_length=256)
    nickname = models.CharField('昵称', max_length=32)
    status = models.SmallIntegerField('用户状态', choices=USER_STATUS, default=1)
    created_at = models.DateTimeField('用户的创建时间', null=True, blank=True)
    remark = models.CharField('备注信息', max_length=256, null=True, blank=True)
    objects = models.Manager()      # 加上这句就可以了
    # users = UserManager()      # 加上这句就可以了
    class Meta:
        db_table = 'weibo_user'

    def __str__(self):
        return 'User:{0},Nickname:{1}'.format(self.username, self.nickname)

class Weibo(models.Model):
    content = models.CharField('微博内容', max_length=500)
    user = models.ForeignKey(WeiboUser, verbose_name='用户')
    created_at = models.DateTimeField('发布时间', auto_now_add=True)
    source = models.CharField('发布来源', max_length=10, null=True, blank=True)
    class Meta:
        db_table = 'weibo'


class WeiboImage(models.Model):
    weibo = models.ForeignKey(Weibo)
    image = models.ImageField(upload_to='weibo', verbose_name='图片')
    class Meta:
        db_table = 'weibo_images'


class Comment(models.Model):
    content = models.CharField('评论内容', max_length=250)
    created_at = models.DateTimeField('评论时间', auto_now_add=True)
    user = models.ForeignKey(WeiboUser, verbose_name='评论的用户')
    weibo = models.ForeignKey(Weibo,verbose_name='关联的微博')
    objects = models.Manager()
    class Meta:
        db_table = 'weibo_comments'

class Friend(models.Model):
    user_from = models.ForeignKey(WeiboUser, verbose_name='关注人', related_name='user_from')
    user_to = models.ForeignKey(WeiboUser, verbose_name='被关注人', related_name='user_to')
    created_at = models.DateTimeField('关注时间', auto_now_add=True)
    class Meta:
        db_table = 'weibo_friends'

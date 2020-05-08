from django.db import models

# Create your models here.
class CommonUtils(models.Model):
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('最后修改时间', auto_now=True)
    class Meta:
        abstract = True

class Student(CommonUtils):
    """学生表"""
    name = models.CharField('姓名', max_length=64)
    sex = models.CharField('性别', max_length=1, choices=(
        ('1', '男'),
        ('0', '女')
    ), default='1')
    id_no = models.CharField('学号', max_length=10, default='1')
    age = models.PositiveIntegerField('年龄', default=0)
    username = models.CharField('登录名', max_length=64, unique=True)
    password = models.CharField('密码', max_length=256)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('最后修改时间', auto_now=True)

    # 内部类
    class Meta:
        varbose_name = '学生表'
        verbose_name_plural = '学生表'
        db_table = 'students'
        ordering = ['-updated_at']

    def get_name(self):
        return self.name[0]


class Course(CommonUtils):
    name = models.CharField('课程名称', max_length=256)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('最后修改时间', auto_now=True)



class ProxyStudent(Student):  #代理模型
    class Meta:
        proxy = True   #代理模型
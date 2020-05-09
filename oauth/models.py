from django.db import models

# Create your models here.
class CommonUtils(models.Model):
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('最后修改时间', auto_now=True)
    class Meta:
        abstract = True

class Course(CommonUtils):
    name = models.CharField('课程名称', max_length=256)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('最后修改时间', auto_now=True)

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
    courses = models.ManyToManyField(Course)

    # 内部类
    class Meta:
        verbose_name = '学生表'
        verbose_name_plural = '学生表'
        db_table = 'students'
        ordering = ['-updated_at']

    def get_name(self):
        return self.name[0]


class UserDetail(models.Model):
    student = models.OneToOneField(Student)
    sign = models.CharField('座右铭', max_length=256)

class UserAddress(CommonUtils):
    user = models.ForeignKey(Student, verbose_name='学生')
    phone = models.CharField('收件人电话', max_length=11)
    address = models.CharField('收件人地址', max_length=64)
    zip_code = models.CharField('邮编', max_length=10, null=True, blank=True)
    is_valid = models.BooleanField('是否有效', default=True)


class ProxyStudent(Student):  #代理模型
    class Meta:
        proxy = True   #代理模型


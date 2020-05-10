from django.db import models

# Create your models here.
from utils import constants


class Slider(models.Model):

    object = models.Manager()
    name = models.CharField('名称', max_length=32)
    desc = models.CharField('描述', max_length=100, null=True, blank=True)
    types = models.SmallIntegerField('展现位置', choices=constants.SLIDER_TYPES_CHOICES, default=constants.SLIDER_TYPE_INDEX)
    img = models.ImageField('图片', upload_to='slider')
    reorder = models.SmallIntegerField('排序', default=0, help_text='数字越大，越靠前')
    start_time = models.DateTimeField('生效开始时间', null=True, blank=True)
    end_time = models.DateTimeField('生效结束时间', null=True, blank=True)
    target_url = models.CharField('跳转地址', null=True, blank=True)
    is_valid = models.BooleanField('是否删除', default=True)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('最后修改时间', auto_now=True)
    class Meta:
        db_table = 'system_slider'
        ordering = ['-reorder']

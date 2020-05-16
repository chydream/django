import uuid

from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

# Create your models here.
from accounts.models import User
from oauth.models import Student
from system.models import ImageFile
from utils import constants

class Classify(models.Model):
    uid = models.UUIDField('分类ID', default=uuid.uuid4, editable=True)
    parent = models.ForeignKey('self',related_name='children')
    img = models.ImageField('分类主图', upload_to='classify')
    code = models.CharField('编码', max_length=32, null=True, blank=True)
    name = models.CharField('名称', max_length=12)
    desc = models.CharField('描述',max_length=64, null=True, blank=True)
    reorder = models.SmallIntegerField('排序', default=0)
    is_valid = models.BooleanField('是否有效', default=True)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('修改时间', auto_now=True)
    class Meta:
        db_table = 'mall_classify'


class Tag(models.Model):
    uid = models.UUIDField('标签ID', default=uuid.uuid4, editable=True)
    img = models.ImageField('主图', upload_to='tags', null=True, blank=True)
    code = models.CharField('编码', max_length=32, null=True, blank=True)
    name = models.CharField('名称', max_length=12)
    reorder = models.SmallIntegerField('排序', default=0)
    is_valid = models.BooleanField('是否有效', default=True)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('修改时间', auto_now=True)
    class Meta:
        db_table = 'mall_tag'


class Product(models.Model):
    objects = models.Manager
    uid = models.UUIDField('商品ID', default=uuid.uuid4, editable=False)
    name = models.CharField('商品名称', max_length=128)
    desc = models.CharField('简单描述', max_length=256, null=True, blank=True)
    content = models.TextField('商品描述',default='1')
    types = models.SmallIntegerField('商品类型',choices=constants.PRODUCT_TYPES_CHOICES, default=constants.PRODUCT_TYPE_ACTUAL)
    price = models.IntegerField('兑换价格(积分兑换)')
    origin_price = models.FloatField('原价')
    img = models.ImageField('主图', upload_to='%Y%m/product')
    buy_link = models.CharField('购买链接', max_length=256, null=True,blank=True)
    reorder = models.SmallIntegerField('排序', default=0)
    status = models.SmallIntegerField('商品状态', default=constants.PRODUCT_STATUS_LOST, choices=constants.PRODUCT_STATUS_CHOICES)
    sku_count = models.IntegerField('库存', default=0)
    remain_count = models.IntegerField('剩余库存', default=0)
    view_count = models.IntegerField('浏览次数', default=0)
    score = models.FloatField('商品的评分', default=10.0)
    is_valid = models.BooleanField('是否有效', default=True)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('修改时间', auto_now=True)
    tags = models.ManyToManyField(Tag, verbose_name='标签', related_name='tags', null=True, blank=True)
    classes = models.ManyToManyField(Classify, verbose_name='分类', related_name='classes', null=True, blank=True)
    banners = GenericRelation(ImageFile, verbose_name='banner图', related_query_name='banners')


    class Meta:
        db_table = 'mall_product'
        ordering = ['-reorder']
        verbose_name = '商品信息'
        verbose_name_plural = '商品信息'


    def __str__(self):
        return self.name
    # collections = GenericRelation('Collection')




# class Store(models.Model):
#     name = models.CharField('店铺名称', max_length=64)
#
# class Collection(models.Model):
#     user = models.ForeignKey(Student)
#     content_type = models.ForeignKey(ContentType)
#     object_id = models.IntegerField('关联的ID')
#     content_object = GenericForeignKey('content_type', 'object_id')
#     created_at = models.DateTimeField('收藏时间', auto_now_add=True)

from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

# Create your models here.
from oauth.models import Student


class Product(models.Model):
    name = models.CharField('商品名称', max_length=64)
    collections = GenericRelation('Collection')

class Store(models.Model):
    name = models.CharField('店铺名称', max_length=64)

class Collection(models.Model):
    user = models.ForeignKey(Student)
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField('关联的ID')
    content_object = GenericForeignKey('content_type', 'object_id')
    created_at = models.DateTimeField('收藏时间', auto_now_add=True)

from django.contrib import admin

# Register your models here.
from mall.forms import ProductAdminForm
from mall.models import Product, Classify, Tag
from utils.admin_actions import set_invalid, set_valid


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # fields =
    # exclude =
    # form =
    # ordering =
    list_display = ['name', 'types', 'price', 'status', 'is_valid']
    list_per_page = 5
    list_filter = ('types', 'status', )
    # search_fields = ('name', )
    actions = [set_invalid, set_valid]
    readonly_fields = ['remain_count']
    # exclude = ['remain_count']
    form = ProductAdminForm

# admin.site.register(Product, ProductAdmin)


@admin.register(Classify)
class ClassifyAdmin(admin.ModelAdmin):
    list_display = ('parent', 'name', 'code', 'is_valid')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_valid', 'code')
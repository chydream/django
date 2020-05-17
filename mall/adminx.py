import xadmin


from mall.models import Product


class ProductAdmin(object):
    list_display = ['name', 'types', 'price', 'is_valid']
    list_filter = ('types', 'is_valid')
    search_fields = ('name',)


xadmin.site.register(Product, ProductAdmin)
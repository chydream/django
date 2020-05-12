SLIDER_TYPE_INDEX = 11
SLIDER_TYPES_CHOICES = (
    (11, '首页'),
)

NEWS_TYPE_NEW=11
NEWS_TYPE_NOTICE=12
NEWS_TYPES_CHOICES=(
    (NEWS_TYPE_NEW, '新闻'),
    (NEWS_TYPE_NOTICE, '通知'),
)

PRODUCT_TYPE_ACTUAL = 11
PRODUCT_TYPE_VIRTUAL = 12
PRODUCT_TYPES_CHOICES = (
    (PRODUCT_TYPE_ACTUAL, '实物商品'),
    (PRODUCT_TYPE_VIRTUAL, '虚拟商品')
)

PRODUCT_STATUS_SELL = 11
PRODUCT_STATUS_LOST = 12
PRODUCT_STATUS_OFF = 13
PRODUCT_STATUS_CHOICES = (
    (PRODUCT_STATUS_SELL, '销售中'),
    (PRODUCT_STATUS_LOST, '已售完'),
    (PRODUCT_STATUS_OFF, '已下架'),
)


ORDER_STATUS_INIT = 10
ORDER_STATUS_SUBMIT = 11
ORDER_STATUS_PAIED = 12
ORDER_STATUS_SEND = 13
ORDER_STATUS_DONE = 14
ORDER_STATUS_DELETE = 15
ORDER_STATUS_CHOICES = (
    (ORDER_STATUS_INIT, '购物车'),
    (ORDER_STATUS_SUBMIT, '已提交'),
    (ORDER_STATUS_PAIED, '已支付'),
    (ORDER_STATUS_SEND, '已发货'),
    (ORDER_STATUS_DONE, '已完成'),
    (ORDER_STATUS_DELETE, '已删除'),
)

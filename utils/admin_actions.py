from django.contrib import messages


def set_invalid(modeladmin, request, queryset):
    queryset.update(is_valid=False)
    messages.success(request, '操作成功')


set_invalid.short_description = '逻辑删除所选对象'


def set_valid(modeladmin, request, queryset):
    queryset.update(is_valid=True)
    messages.success(request, '操作成功')


set_valid.short_description = '逻辑启用所选对象'
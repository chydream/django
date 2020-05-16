from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from accounts.models import User

@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('format_username', 'nickname', 'integral', 'is_active')
    search_fields = ('username', 'nickname')
    actions = ['disable_user', 'enable_user']  # 添加自定义方法

    def format_username(self, obj):
        return obj.username[0:3] + "***"
    format_username.short_description = '用户名'


    def disable_user(self, request, queryset):
        queryset.update(is_active=False)
    disable_user.short_description = '批量禁用用户'

    def enable_user(self, request, queryset):
        queryset.update(is_active=True)
    enable_user.short_description = '批量启用用户'

# admin.site.register(User, UserAdmin)

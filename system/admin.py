from django.contrib import admin

# Register your models here.
from system.models import News, Slider
from utils.admin_actions import set_valid, set_invalid


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'types', 'is_valid')
    actions = [set_valid, set_invalid]

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('name', 'types', 'start_time', 'end_time', 'is_valid')
    actions = [set_valid, set_invalid]
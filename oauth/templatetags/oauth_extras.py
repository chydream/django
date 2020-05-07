from django import template
register = template.Library()

def warning(value):
    if value:
        return '<span style="color:red">' + value[0] + '</span>' + value[1:]
    return value


def money_format(value):
    return format(value, '0,.2f')

register.filter('warning', warning)
register.filter('money_format', money_format)
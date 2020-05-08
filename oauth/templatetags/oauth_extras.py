import locale
from decimal import Decimal

from django import template
register = template.Library()

def warning(value):
    if value:
        return '<span style="color:red">' + value[0] + '</span>' + value[1:]
    return value


def money_format(value):
    return format(value, '0,.2f')

def accounting(value, place=2):
    try:
        place = int(place)
    except:
        place = 2

    try:
        value = Decimal(value)
        locale.setlocale(locale.LC_ALL, '')
        return locale.format("%.*f", (place, value), 1)
    except Exception as e:
        return value

register.filter('warning', warning)
register.filter('money_format', money_format)
register.filter('accounting', accounting)
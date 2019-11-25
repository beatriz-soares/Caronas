import re
from django import template
register = template.Library()


@register.filter(name='add_css_class')
def add_css_class(value, arg):
    return value.as_widget(attrs={'class': arg})

from django import template
from django.contrib.staticfiles.finders import find
register = template.Library()

@register.filter
def static_exists(path):
    return find(path) is not None 
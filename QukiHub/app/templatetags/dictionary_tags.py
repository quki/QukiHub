from django import template

register = template.Library()

# https://www.youtube.com/watch?v=MsLg_NFAHLk


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

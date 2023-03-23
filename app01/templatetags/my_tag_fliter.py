__author__ = 'Administrator'


from  django import template

register=template.Library()
@register.filter
def multi_filter(x,y=2):
    return x*y
from django import template

# requests = template.Library()
register = template.Library()

@register.filter()
def mymedia(val):
    if val:
        return f'/media/{val}'
    return '#'

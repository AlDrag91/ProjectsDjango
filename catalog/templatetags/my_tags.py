from django import template

requests = template.Library()


@requests.filter()
def mymedia(val):
    if val:
        return f'/media/{val}'
    return '#'

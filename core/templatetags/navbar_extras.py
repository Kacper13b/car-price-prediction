from django import template


register = template.Library()


def is_logged(is_authenticated: bool):
    if is_authenticated:
        return 'invisible'
    else:
        return ''


register.filter("logged", is_logged)

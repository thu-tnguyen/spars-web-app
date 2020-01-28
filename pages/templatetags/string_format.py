from django import template
register = template.Library()
def string_format(value):
    """Replaces empty space in form of ' ' with '+'. 
    Used for search involving spaces."""
    return value.replace(' ', '+')

register.filter('string_format', string_format)
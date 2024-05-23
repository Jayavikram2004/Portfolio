from django import template

register = template.Library()

@register.filter
def filesizeformatmb(value):
    """Converts a file size in bytes to megabytes (MB) and formats to 2 decimal places"""
    mb_value = value / (1024 * 1024)
    return f'{mb_value:.2f} MB'

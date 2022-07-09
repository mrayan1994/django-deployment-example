from django import template

register = template.Library()


@register.filter('remove_all_char')
def remove_all_char_from_str(str, char):
    """
    This cuts out all values of "char" from the string
    """
    return str.replace(char, '')


# register.filter('remove_all_char', remove_all_char_from_str)

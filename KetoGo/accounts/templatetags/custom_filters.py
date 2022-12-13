from django import template

register = template.Library()


@register.filter
def placeholder(value, text):
    value.field.widget.attrs['placeholder'] = text
    return value


@register.filter(name='is_in_perm_group')
def is_in_perm_group(user, group_name):
    return user.groups.filter(name=group_name).exists()

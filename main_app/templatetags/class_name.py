from django import template
from main_app.models import *
from login_reg_app.models import *
register = template.Library()
print(10)

@register.filter()
def class_name(value):
    print(11)
    return value.__class__.__name__
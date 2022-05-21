from django import template
from app.models import *

register = template.Library()


@register.inclusion_tag('app/list_categories.html')
def show_categories(sort=None, reg_selected=0):
    if not sort:
        regions = Region.objects.all()
    else:
        regions = Region.objects.order_by(sort)

    return {"regions": regions, "reg_selected": reg_selected}

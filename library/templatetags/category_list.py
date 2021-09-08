from django import template
from library.models import CategoriesModel

register = template.Library()

@register.simple_tag
def category_list():
    all_categories = CategoriesModel.objects.all()
    return all_categories
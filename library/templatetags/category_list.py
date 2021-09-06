from django import template
from library.models import CategoriesModel, categories

register = template.Library()

@register.simple_tag
def category_list():
    categories = CategoriesModel.objects.all()
    return categories
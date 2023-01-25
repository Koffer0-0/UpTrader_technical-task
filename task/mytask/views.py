from django.http import HttpResponse
from django.template import loader
from .models import Item, Category, SubCategory
# Create your views here.


def index(request, parent_or_child=None, pk=None):
    categories = Category.object.filter(parent=None)
    if parent_or_child is None:
        items = Item.objects.all()

    elif parent_or_child == 'child':
        subCategory = SubCategory.objects.get(pk=pk)
        items = subCategory.item_set.all()

    elif parent_or_child == 'parent':
        subCategories = SubCategory.objects.get(pk=pk).children.all()
        items = []

        for subCategory in subCategories:
            item = subCategory.item_set.all()
            items += item
    else:
        items = []

    template = loader.get_template('index.html')
    context = {
        'categories': categories,
        'items': items,

    }
    return HttpResponse(template.render(context, request))


def base(request, parent_or_child=None, pk=None):
    subCategory = SubCategory.object.filter(pk=pk)
    category = Category.object.filter(pk=pk)
    items = []
    if parent_or_child == 'child':
        for sub in subCategory:
            item = sub.item_set.all()
            items += item

    elif parent_or_child == 'parent':
        subCategories = SubCategory.objects.get(pk=pk).children.all()

        for subs in subCategories:
            item = subs .item_set.all()
            items += item

    template = loader.get_template('base.html')
    context = {
        'subCategory': subCategory,
        'category': category,
        'items': items,

    }
    return HttpResponse(template.render(context, request))
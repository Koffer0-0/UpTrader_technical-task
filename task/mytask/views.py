from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.views.generic import ListView

# from mytask.models import MenuItems, MenuCategories


# def index(request):
#     template = loader.get_template('index.html')
#     context = {}
#     return HttpResponse(template.render(context, request))

#
# def get_gategories_list():
#     categories_list = CategoryPage.objects.live().order_by('name')
#
#     def tree(objects):
#         depth = min([obk])
#
#     return tree(categories_list ) if categories_list else []
#
#
# class CategoriesListView(ListView):
#     model = MenuCategories
#     template_name = "categories.html"
#
#
# class ItemsByCategoryView(ListView):
#     context_object_name = 'items'
#     template_name = 'items.html'
#
#     def get_queryset(self):
#         self.item = MenuCategories.objects.get(slug=self.kwargs['slug'])
#         queryset = MenuItems.objects.filter(category=self.item)
#         return queryset
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = self.item
#         return context
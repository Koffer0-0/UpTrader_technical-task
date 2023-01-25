from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Item, Category, SubCategory


# Register your models here.
class SubCategoryInline(admin.TabularInline):
    model = SubCategory
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    list_editable = ('parent',)
    fieldsets = (
        (
            None,
            {
                'fields': ('name',)
            }
        ),
    )
    inlines = (SubCategoryInline,)


admin.site.register(Category, CategoryAdmin)


class ItemInline(admin.TabularInline):
    model = Item
    extra = 1


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('parent', 'name', 'product_count')
    fieldsets = (
        (
            None,
            {
                'fields': ('name',)
            }
        ),
    )
    inlines = (ItemInline,)

    def product_count(self, obj):
        return obj.item_set.count()

    def get_ordering(self, request):
        return ('parent', 'name')


admin.site.register(SubCategory, SubCategoryAdmin)

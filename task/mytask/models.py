from django.db import models
from .managers import CategoryManager, SubCategoryManager
# Create your models here.


# model
class Node(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Nodes'


# proxy category model
class Category(Node):
    object = CategoryManager()
    class Meta:
        proxy = True
        verbose_name_plural = 'Categories'


# proxy sub category model
class SubCategory(Node):
    object = SubCategoryManager()
    class Meta:
        proxy = True
        verbose_name_plural = 'sub categories'


# item
class Item(models.Model):
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name

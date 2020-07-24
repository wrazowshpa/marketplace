from django.forms import ModelForm
from .models import Ad, Category, Subcategory, Subsubcategory
from django import forms

'''
class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('category_name',)


class SubCategoryForm(ModelForm):
    class Meta:
        model = Subcategory
        fields = ('sub_category_name',)


class SubSubCategoryForm(ModelForm):
    class Meta:
        model = Subsubcategory
        fields = ('sub_sub_category_name',)


class AdForm(ModelForm):
    class Meta:
        model = Ad
        fields = ('category', 'author', 'ad_title', 'description', 'region', 'price', 'phone_number')
'''

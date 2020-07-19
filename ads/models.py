import uuid
from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=400)

    def __str__(self):
        return self.category_name


class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategory')
    sub_category_name = models.CharField(max_length=400)

    def __str__(self):
        return self.sub_category_name


class Subsubcategory(models.Model):
    sub_category = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='subsubcategory')
    sub_sub_category_name = models.CharField(max_length=400)

    def __str__(self):
        return self.sub_sub_category_name






from django.contrib import admin
from .models import Category, Subcategory, Subsubcategory, Ad, AdImage


# Register your models here.
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Subsubcategory)
admin.site.register(Ad)
admin.site.register(AdImage)


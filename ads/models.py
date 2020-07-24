import uuid
from django.db import models
from django.conf import settings
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


class Ad(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='ad')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, db_column='email', on_delete=models.CASCADE)
    ad_title = models.CharField(max_length=400)
    description = models.TextField(max_length=6000)
    region = models.CharField(max_length=200)
    price = models.IntegerField()
    phone_number = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.localtime(timezone.now()))

    def __str__(self):
        return self.ad_title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': str(self.pk)})


class AdImage(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='postimage')
    image = models.ImageField(upload_to='images/ad', verbose_name='image',)

    def __str__(self):
        return str(self.image)










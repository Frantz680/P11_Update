from django.db import models
from django.contrib.auth.models import User


class Category_product(models.Model):
    name_category = models.CharField(max_length=100)


class Name(models.Model):
    name_product = models.CharField(max_length=250, unique=True)
    category = models.ForeignKey(
        Category_product, on_delete=models.CASCADE, default='None')
    nutrition_grade = models.CharField(default='E', max_length=1)
    picture_product = models.URLField(default='None')
    picture_nutrition = models.URLField(default='None')
    url_product = models.URLField(default='None')


class My_product_save(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Name, on_delete=models.CASCADE)

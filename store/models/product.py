from django.db import models
from .category import Category

class Product (models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200, default='', null = True, blank=True)
    image = models.ImageField(upload_to='uploads/products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    @staticmethod
    def get_all_products():
        return Product.objects.all()
    
    @staticmethod
    def get_products_by_CategoryId(category_Id):
        if category_Id:
            return Product.objects.filter(category = category_Id)
        else:
            return Product.get_all_products()          

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in =ids)
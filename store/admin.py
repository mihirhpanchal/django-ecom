from store.models.customer import Customer
from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
# Register your models here.


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

class Customers(admin.ModelAdmin):
    list_display = ['firstName','lastName','phone','email','password']

class Orders(admin.ModelAdmin):
    list_display = ['customer','quantity','price','date','status']
    
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer, Customers)
admin.site.register(Order, Orders)
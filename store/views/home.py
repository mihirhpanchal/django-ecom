from store.models.category import Category
from django.shortcuts import redirect, render
from django.http import HttpResponse
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import View

class Index(View):
    def get(self, request):
        products = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_products_by_CategoryId(categoryID)
        else:
            products = Product.get_all_products()
        data = {}
        data['categories'] = categories
        data['products'] = products
        print("You are: ", request.session.get('email'))
        return render(request, 'index.html', data)

    def post(self, request):
        product = request.POST.get('product')
        print (product)
        return redirect('homepage')
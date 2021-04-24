from store.models.category import Category
from django.shortcuts import redirect, render
from django.http import HttpResponse
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import View

class Index(View):
    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
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
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('homepage')
from functools import singledispatch
from store.views.order import OrderView
from store.models.orders import Order
from store.views.checkout import CheckOut
from store.views.cart import Cart
from django.urls import path, include
from store.views.home import Index
from store.views.signup import Signup
from store.views.login import Login, logout
from .middlewares.auth import auth_middleware


urlpatterns = [
    path('', Index.as_view(), name = 'homepage'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout ),
    path('cart', Cart.as_view(), name = 'cart'),
    path('check-out', CheckOut.as_view(), name = 'checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name = 'orders'),
]

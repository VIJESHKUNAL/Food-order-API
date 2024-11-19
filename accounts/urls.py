# accounts/urls.py
from django.urls import path
from .views import register_view, login_view, add_to_cart,get_cart_items,remove_cart_item, proceed_to_checkout

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('cart/add/', add_to_cart, name='add-to-cart'),
    path('cart/', get_cart_items, name='get-cart-items'),
    path('cart/remove/<int:item_id>/', remove_cart_item, name='remove-cart-item'),
    path('cart/checkout/', proceed_to_checkout, name='proceed-to-checkout'),

]


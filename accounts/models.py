# # models.py
# from django.db import models

# class CartItem(models.Model):
#     name = models.CharField(max_length=255)
#     image_url = models.URLField(max_length=1024)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     quantity = models.IntegerField(default=1)
#     cart_or_ordered = models.CharField(max_length=1, default='C')

#     def __str__(self):
#         return self.name


# models.py
from django.db import models
from django.contrib.auth.models import User

class CartItem(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.URLField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    cart_or_ordered = models.CharField(max_length=1, choices=[('C', 'Cart'), ('O', 'Ordered')], default='C')
    user_email = models.EmailField()  # Link the cart item to the user's email

    def __str__(self):
        return f"{self.name} ({self.quantity})"


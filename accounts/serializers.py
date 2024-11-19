# accounts/serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import CartItem

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user



class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model  = CartItem
        fields = ['id', 'name', 'image_url', 'description', 'price', 'quantity', 'cart_or_ordered', 'user_email']


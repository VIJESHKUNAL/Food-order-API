# # accounts/views.py
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from django.contrib.auth.models import User
# from .serializers import RegisterSerializer

# from django.contrib.auth import authenticate
# from rest_framework import status

# @api_view(['POST'])
# def register_view(request):
#     serializer = RegisterSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# def login_view(request):
#     username = request.data.get('username')
#     password = request.data.get('password')

#     user = authenticate(username=username, password=password)
#     if user is not None:
#         return Response({'message': 'Login successful', 'username': user.username}, status=status.HTTP_200_OK)
#     else:
#         return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


# accounts/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from .serializers import RegisterSerializer

# Registration API view
@api_view(['POST'])
def register_view(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()  # Saves the user in the MySQL database
        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # Login API view
# @api_view(['POST'])
# def login_view(request):
#     username = request.data.get('username')
#     password = request.data.get('password')

#     user = authenticate(username=username, password=password)  # Checks against MySQL database
#     if user is not None:
#         return Response({'message': 'Login successful', 'username': user.username}, status=status.HTTP_200_OK)
#     else:
#         return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


# accounts/views.py


# @api_view(['GET'])
# def login_view(request):
#     # Retrieve 'username' and 'password' from headers
#     username = request.headers.get('Username')  # Custom header
#     password = request.headers.get('Password')  # Custom header

#     # Check if username and password are provided
#     if not username or not password:
#         return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

#     # Authenticate the user using the provided credentials
#     user = authenticate(username=username, password=password)

#     # If user is found, return a success response
#     if user is not None:
#         return Response({'message': 'Login successful', 'username': user.username}, status=status.HTTP_200_OK)

#     # If authentication fails, return an error
#     return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)



from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
# views.py
from .models import CartItem

from .serializers import CartItemSerializer

@csrf_exempt
@api_view(['GET'])
def login_view(request):
    # Retrieve 'email' and 'password' from headers
    email = request.headers.get('Email')  # Custom header for email
    password = request.headers.get('Password')  # Custom header for password

    # Check if email and password are provided
    if not email or not password:
        return Response({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)

    # Authenticate the user using the provided email and password
    user = authenticate(username=email, password=password)  # 'username' should hold email in custom backend

    # If user is found, return a success response
    if user is not None:
        return Response({'message': 'Login successful', 'email': user.email}, status=status.HTTP_200_OK)

    # If authentication fails, return an error
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])
def add_to_cart(request):
    # Get the data from the request
    data = request.data
    name = data.get('name')
    image_url = data.get('image_url')
    description = data.get('description')
    price = data.get('price')
    quantity = data.get('quantity')
    cart_or_ordered = data.get('cart_or_ordered')
    user_email = data.get('user_email')

    # Validate that required fields are present
    if not name or not price or not quantity:
        return Response({"error": "Name, price, and quantity are required."}, status=status.HTTP_400_BAD_REQUEST)

    # Create a new CartItem object and save it to the database
    cart_item = CartItem.objects.create(
        name=name,
        image_url=image_url,
        description=description,
        price=price,
        quantity=quantity,
        cart_or_ordered=cart_or_ordered,
        user_email=user_email
    )
    cart_item.save()

    return Response({"message": "Item added to cart successfully!"}, status=status.HTTP_201_CREATED)


# views.py


# @api_view(['GET'])
# def get_cart_items(request):
#     # Fetch all cart items from the database
#     cart_items = CartItem.objects.all()
#     serializer = CartItemSerializer(cart_items, many=True)
#     return Response(serializer.data)


@api_view(['DELETE'])
def remove_cart_item(request, item_id):
    try:
        cart_item = CartItem.objects.get(id=item_id)
        cart_item.delete()
        return Response({"message": "Item removed from cart successfully"}, status=status.HTTP_204_NO_CONTENT)
    except CartItem.DoesNotExist:
        return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def proceed_to_checkout(request):
    user_email = request.data.get('email')
    if not user_email:
        return Response({"error": "User email is required"}, status=status.HTTP_400_BAD_REQUEST)

    # Find all cart items of the user that are still in the cart ('C') and update to ordered ('O')
    cart_items = CartItem.objects.filter(user_email=user_email, cart_or_ordered='C')
    if cart_items.exists():
        cart_items.update(cart_or_ordered='O')
        return Response({"message": "Items successfully checked out"}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "No cart items to checkout"}, status=status.HTTP_400_BAD_REQUEST)
99

# views.py
@api_view(['GET'])
def get_cart_items(request):
    user_email = request.headers.get('Email')  # Get the user email from headers (or wherever you're storing it)
    if not user_email:
        return Response({"error": "User email is required"}, status=status.HTTP_400_BAD_REQUEST)

    # Fetch only the cart items for the logged-in user
    cart_items = CartItem.objects.filter(user_email=user_email, cart_or_ordered='C')
    serialized_data = [{"id": item.id, "name": item.name, "image_url": item.image_url, "description": item.description, "price": item.price, "quantity": item.quantity} for item in cart_items]
    
    return Response(serialized_data, status=status.HTTP_200_OK)

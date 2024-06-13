from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField(null=True, default=None)
    profile_picture = models.ImageField(
        upload_to="profile_pictures/", null=True, blank=True
    )
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username


class Restaurant(models.Model):
    # Represents a restaurant in the system
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    description = models.TextField()
    logo = models.ImageField(upload_to="restaurant_logos/", null=True, blank=True)


class MenuItem(models.Model):
    # Represents a menu item offered by a restaurant
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to="menu_item_images/", null=True, blank=True)


class Order(models.Model):
    # Represents an order made by a user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    # Represents an item within an order
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


class DeliveryAddress(models.Model):
    # Represents a delivery address associated with a user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    is_default = models.BooleanField(default=False)


class PaymentInformation(models.Model):
    # Represents payment information associated with a user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16)
    expiration_date = models.DateField()
    is_default = models.BooleanField(default=False)


class Review(models.Model):
    # Represents a review/rating given by a user to a restaurant
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Cuisine(models.Model):
    # Represents a cuisine offered by a restaurant
    name = models.CharField(max_length=100)


class Discount(models.Model):
    # Represents a discount coupon
    code = models.CharField(max_length=20, unique=True)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()


class DeliveryPersonnel(models.Model):
    # Represents a delivery person associated with the restaurant
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    vehicle_number = models.CharField(max_length=20)


class OperatingHours(models.Model):
    # Represents the operating hours of a restaurant
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10)
    opening_time = models.TimeField()
    closing_time = models.TimeField()


class FoodCategory(models.Model):
    # Represents a category of food
    name = models.CharField(max_length=100)
    description = models.TextField()

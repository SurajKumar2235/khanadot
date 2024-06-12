# myapp/admin.py

from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "phone_number", "date_of_birth")
    search_fields = ("username", "email")
    list_filter = ("date_of_birth",)


class OperatingHoursInline(admin.TabularInline):
    model = OperatingHours
    extra = 1


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "description")
    search_fields = ("name", "address")
    list_filter = ("name",)
    inlines = [OperatingHoursInline]


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "restaurant", "description")
    search_fields = ("name", "restaurant__name")
    list_filter = ("restaurant",)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "total_amount", "timestamp")
    search_fields = ("user__username", "user__email")
    list_filter = ("timestamp",)
    inlines = [OrderItemInline]


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "menu_item", "quantity")
    search_fields = ("order__user__username", "menu_item__name")


class DeliveryAddressAdmin(admin.ModelAdmin):
    list_display = ("user", "address", "is_default")
    search_fields = ("user__username", "address")


class PaymentInformationAdmin(admin.ModelAdmin):
    list_display = ("user", "card_number", "expiration_date", "is_default")
    search_fields = ("user__username", "card_number")


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("user", "restaurant", "rating", "timestamp")
    search_fields = ("user__username", "restaurant__name")
    list_filter = ("rating", "timestamp")


class CuisineAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class DiscountAdmin(admin.ModelAdmin):
    list_display = ("code", "discount_percent", "start_date", "end_date")
    search_fields = ("code",)
    list_filter = ("start_date", "end_date")


class DeliveryPersonnelAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number", "vehicle_number")
    search_fields = ("name", "phone_number")


class OperatingHoursAdmin(admin.ModelAdmin):
    list_display = ("restaurant", "day_of_week", "opening_time", "closing_time")
    search_fields = ("restaurant__name", "day_of_week")
    list_filter = ("day_of_week",)


class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)


admin.site.register(User, UserAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(DeliveryAddress, DeliveryAddressAdmin)
admin.site.register(PaymentInformation, PaymentInformationAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Cuisine, CuisineAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(DeliveryPersonnel, DeliveryPersonnelAdmin)
admin.site.register(OperatingHours, OperatingHoursAdmin)
admin.site.register(FoodCategory, FoodCategoryAdmin)

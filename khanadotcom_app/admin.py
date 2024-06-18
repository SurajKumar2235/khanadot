from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone_number", "user_type", "created_at")
    search_fields = ("name", "email", "phone_number")
    list_filter = ("user_type", "created_at")


class CustomerDetailsAdmin(admin.ModelAdmin):
    list_display = ("customer", "name", "phone_number", "address")
    search_fields = ("customer__name", "phone_number", "address")
    list_filter = ("customer__created_at",)


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "address", "phone_number", "email", "rating")
    search_fields = ("name", "owner__name", "phone_number", "email")
    list_filter = ("rating", "created_at")


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "restaurant", "availability", "rating")
    search_fields = ("name", "restaurant__name")
    list_filter = ("restaurant", "availability", "created_at")


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "total_amount", "order_status", "order_date", "delivery_date")
    search_fields = ("user__name", "user__email")
    list_filter = ("order_status", "order_date", "delivery_date")
    inlines = [OrderItemInline]


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "menu_item", "quantity", "price")
    search_fields = ("order__user__name", "menu_item__name")
    list_filter = ("order__order_date",)


class PaymentAdmin(admin.ModelAdmin):
    list_display = ("order", "payment_method", "amount", "payment_status", "payment_date")
    search_fields = ("order__user__name", "payment_method", "transaction_id")
    list_filter = ("payment_status", "payment_date")


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("user", "restaurant", "delivery_person", "rating", "created_at")
    search_fields = ("user__name", "restaurant__name", "delivery_person__user__name")
    list_filter = ("rating", "created_at")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)
    list_filter = ("created_at",)


class MenuItemCategoryAdmin(admin.ModelAdmin):
    list_display = ("menu_item", "category")
    search_fields = ("menu_item__name", "category__name")
    list_filter = ("created_at",)


class NotificationAdmin(admin.ModelAdmin):
    list_display = ("user", "message", "created_at", "is_read")
    search_fields = ("user__name", "message")
    list_filter = ("created_at", "is_read")


class CouponAdmin(admin.ModelAdmin):
    list_display = ("code", "discount_percentage", "max_discount_amount", "valid_from", "valid_to", "active")
    search_fields = ("code",)
    list_filter = ("valid_from", "valid_to", "active")


class DeliveryPersonAdmin(admin.ModelAdmin):
    list_display = ("user", "vehicle_details", "availability_status", "rating", "created_at")
    search_fields = ("user__name", "vehicle_details")
    list_filter = ("availability_status", "created_at")


admin.site.register(User, UserAdmin)
admin.site.register(CustomerDetails, CustomerDetailsAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(MenuItemCategory, MenuItemCategoryAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(Coupon, CouponAdmin)
admin.site.register(DeliveryPerson, DeliveryPersonAdmin)

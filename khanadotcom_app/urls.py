from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("success/", views.success, name="success"),
    path("signup/", views.signup_api, name="signup_api"),
    path("login/", views.login_api, name="login_api"),
    path("logout/", views.logout_api, name="logout_api"),
    path("activate/<uidb64>/<str:token>/", views.activate_api, name="activate_api"),
    path("profile/", views.user_profile_api, name="user_profile_api"),
    path("restaurants/", views.restaurant_list_api, name="restaurant_list_api"),
    path(
        "restaurants/<int:restaurant_id>/",
        views.restaurant_detail_api,
        name="restaurant_detail_api",
    ),
    path(
        "restaurants/<int:restaurant_id>/menu/",
        views.menu_items_api,
        name="menu_items_api",
    ),
    path(
        "restaurants/<int:restaurant_id>/order/",
        views.order_placement_api,
        name="order_placement_api",
    ),
    path(
        "order/<str:order_id>/",
        views.order_confirmation_api,
        name="order_confirmation_api",
    ),
    path("order/history/", views.order_history_api, name="order_history_api"),
    # Password reset paths
    path("password-reset/", views.request_password_reset, name="password_reset"),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        views.password_reset_confirm,
        name="password_reset_confirm",
    ),
    # path(
    #     "restaurant_owner/update/",
    #     views.update_restaurant_owner_details,
    #     name="update_restaurant_owner_details",
    # ),
    # path(
    #     "delivery_person/update/",
    #     views.update_delivery_person_details,
    #     name="update_delivery_person_details",
    # ),
    # path(
    #     "restaurant/<int:restaurant_id>/update/",
    #     views.update_restaurant_details,
    #     name="update_restaurant_details",
    # ),
]

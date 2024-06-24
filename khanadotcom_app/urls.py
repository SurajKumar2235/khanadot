from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
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
    path(
        "password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]

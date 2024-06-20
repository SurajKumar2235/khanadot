from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .models import *
from .tokens import account_activation_token
from .form import *
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from stdnum.in_ import aadhaar

User = get_user_model()


@login_required(login_url="login")
def home_page(request):
    return render(request, "home.html")


def signup_page(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # User is not active until they confirm their email
            user.save()

            # Send activation email
            send_activation_email(request, user)

            # Redirect to a success page or login page
            return redirect("login")
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form": form})


def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(
                    "home"
                )  # Redirect to home page or wherever you want after login
        # Handle invalid login details here (optional)
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def logout_page(request):
    logout(request)
    return redirect("login")  # Redirect to login page after logout


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect("login")  # Redirect to login page after successful activation
    else:
        return HttpResponse("Activation link is invalid or expired.")


def send_activation_email(request, user):
    mail_subject = "Activate your account."
    message = render_to_string(
        "activate_account.html",
        {
            "user": user,
            "domain": get_current_site(request).domain,
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "token": account_activation_token.make_token(user),
        },
    )
    to_email = user.email
    email = EmailMessage(mail_subject, message, to=[to_email])
    email.send()


# user side
@login_required(login_url="login")
def user_profile_view(request):
    user = request.user

    context = {
        "user": user,
    }
    return render(request, "user_profile.html", context)


def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    context = {"restaurants": restaurants}
    return render(request, "restaurant_list.html", context)


def restaurant_detail(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    context = {"restaurant": restaurant}
    return render(request, "restaurant_detail.html", context)


def menu_items(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    menu_items = MenuItem.objects.filter(restaurant=restaurant)
    context = {
        "restaurant": restaurant,
        "menu_items": menu_items,
    }
    return render(request, "menu_items.html", context)


@login_required(login_url="login")
def order_placement_view(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    menu_items = MenuItem.objects.filter(restaurant=restaurant, availability=True)

    if request.method == "POST":
        form = OrderForm(restaurant_id, request.POST)
        if form.is_valid():
            # Create Order object
            order = Order.objects.create(
                user=request.user,  # Assuming user is authenticated
                delivery_address=form.cleaned_data["delivery_address"],
                total_amount=0,  # Placeholder for total amount
            )

            # Process each selected menu item in the form
            total_amount = 0

            for item_id in form.cleaned_data["items"]:
                menu_item = get_object_or_404(MenuItem, pk=item_id)
                quantity = 1  # For simplicity, assuming quantity is always 1
                OrderItem.objects.create(
                    order=order,
                    menu_item=menu_item,
                    quantity=quantity,
                    price=menu_item.price,
                )
                total_amount += (
                    menu_item.price
                )  # Accumulate menu item price to total_amount

            # Update total_amount in the Order model
            order.total_amount = total_amount
            order.save()

            # Create Payment object (example: cash on delivery)
            payment = Payment.objects.create(
                order=order,
                payment_method="cash_on_delivery",
                amount=total_amount,
                payment_status="pending",  # Adjust based on actual payment flow
            )

            # Redirect to order confirmation page
            return redirect("order_confirmation", order_id=order.order_id)

    else:
        form = OrderForm(restaurant_id=restaurant_id)

    context = {
        "restaurant": restaurant,
        "menu_items": menu_items,
        "form": form,
    }
    return render(request, "order_placement.html", context)


def order_confirmation_view(request, order_id):
    order = get_object_or_404(Order, order_id=order_id)
    context = {"order": order}
    return render(request, "order_confirmation.html", context)


def order_history_view(request):
    # Fetch orders for the current user (assuming user is authenticated)
    orders = Order.objects.filter(user=request.user).order_by("-order_date")

    context = {
        "orders": orders,
    }
    return render(request, "order_history.html", context)


def validate_aadhaar_view(request):
    if request.method == "POST":
        form = AadhaarValidationForm(request.POST)
        if form.is_valid():
            # If the Aadhaar number is valid, you can proceed with further actions
            aadhaar_number = form.cleaned_data.get("aadhaar_number")
            try:
                validate_aadhar(aadhaar_number)
            except ValidationError as e:
                form.add_error("aadhaar_number", e)
                return render(request, "validate_aadhaar.html", {"form": form})

            # Example: Redirect to a success page or render a success message
            return render(
                request, "aadhaar_success.html", {"aadhaar_number": aadhaar_number}
            )
    else:
        form = AadhaarValidationForm()

    return render(request, "validate_aadhaar.html", {"form": form})


def validate_aadhar(aadhar_number):
    aadhar_number = str(aadhar_number).replace(" ", "")

    if not aadhaar.is_valid(aadhar_number):
        raise ValidationError("Invalid Aadhaar number.")

from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.urls import reverse
from .tokens import (
    account_activation_token,
)  # Assuming you have tokens defined in a tokens.py file

User = get_user_model()


@login_required(login_url="login")
def HomePage(request):
    user = request.user  # Correctly retrieve the logged-in user
    return render(request, "home.html", {"user": user})


def SignupPage(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        email = request.POST.get("email")
        pass1 = request.POST.get("password1")
        pass2 = request.POST.get("password2")
        phone = request.POST.get("phone_number")
        dateofbirth = request.POST.get("date_of_birth")
        profilepic = request.FILES.get("profile_picture")

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not the same!!")

        # Create user but mark as inactive
        my_user = User.objects.create_user(
            username=uname, email=email, password=pass1, is_active=False
        )

        # Save additional fields
        my_user.phone_number = phone
        my_user.date_of_birth = dateofbirth

        if profilepic:
            my_user.profile_picture = profilepic

        my_user.save()

        # Send activation email (you need to implement activateEmail function)
        activateEmail(request, my_user, email)

        return redirect("login")  # Redirect to home or login page after signup

    return render(request, "signup.html")


def LoginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request, username=username, password=password, is_active=True
        )
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return HttpResponse(f"Username or Password is incorrect!!!")

    return render(request, "login.html")


def LogoutPage(request):
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


def activateEmail(request, user, to_email):
    mail_subject = "Activate your user Account"
    message = render_to_string(
        "activate_account.html",
        {
            "user": user.username,
            "domain": get_current_site(request).domain,
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "token": account_activation_token.make_token(user),
            "protocol": "https" if request.is_secure() else "http",
        },
    )
    email = EmailMessage(mail_subject, message, to=[to_email])
    email.send()

    return HttpResponse("Activation email sent successfully.")

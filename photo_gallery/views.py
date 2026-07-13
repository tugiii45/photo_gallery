from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserLoginForm
from .models import *
from django.shortcuts import render, redirect, get_object_or_404

@login_required
def home(request):
    """
    Displays all photos in the gallery.
    """

    photos = Photo.objects.all().order_by("-created_at")

    return render(
        request,
        "photo_gallery/home.html",
        {"photos": photos},
    )

@login_required
def photo_detail(request, photo_id):
    """
    Displays detailed information about a selected photo.
    """

    photo = get_object_or_404(Photo, id=photo_id)

    return render(
        request,
        "photo_gallery/photo_detail.html",
        {"photo": photo},
    )

def register(request):
    """
    Registers a new user account.
    """

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            messages.success(
                request,
                "Your account has been created successfully.",
            )

            return redirect("home")
    else:
        form = UserRegistrationForm()

    return render(
        request,
        "photo_gallery/register.html",
        {"form": form},
    )


def user_login(request):
    """
    Authenticates and logs in an existing user.
    """

    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            messages.success(
                request,
                "You have logged in successfully.",
            )

            return redirect("home")
    else:
        form = UserLoginForm()

    return render(
        request,
        "photo_gallery/login.html",
        {"form": form},
    )


def user_logout(request):
    """
    Logs out the authenticated user.
    """

    logout(request)

    messages.success(
        request,
        "You have logged out successfully.",
    )

    return redirect("login")
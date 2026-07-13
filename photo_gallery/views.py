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
    Displays gallery photos and filters them by tag.
    """

    photos = Photo.objects.all().order_by("-created_at")
    selected_tag = request.GET.get("tag")

    if selected_tag:
        photos = photos.filter(tags__icontains=selected_tag)

    all_photos = Photo.objects.all()
    tags = set()

    for photo in all_photos:
        for tag in photo.tags.split(","):
            tags.add(tag.strip())

    return render(
        request,
        "photo_gallery/home.html",
        {
            "photos": photos,
            "tags": sorted(tags),
            "selected_tag": selected_tag,
        },
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

@login_required
def like_photo(request, photo_id):
    """
    Allows a user to like or remove their like from a photo.
    """

    photo = get_object_or_404(Photo, id=photo_id)

    if request.method == "POST":
        if request.user in photo.likes.all():
            photo.likes.remove(request.user)
        else:
            photo.likes.add(request.user)
            photo.dislikes.remove(request.user)

    return redirect("photo_detail", photo_id=photo.id)


@login_required
def dislike_photo(request, photo_id):
    """
    Allows a user to dislike or remove their dislike from a photo.
    """

    photo = get_object_or_404(Photo, id=photo_id)

    if request.method == "POST":
        if request.user in photo.dislikes.all():
            photo.dislikes.remove(request.user)
        else:
            photo.dislikes.add(request.user)
            photo.likes.remove(request.user)

    return redirect("photo_detail", photo_id=photo.id)


@login_required
def profile(request):
    """
    Displays the authenticated user's profile.
    """

    return render(
        request,
        "photo_gallery/profile.html",
        {"profile": request.user.profile},
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
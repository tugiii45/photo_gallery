from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    """
    Stores additional information for each registered user.
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    bio = models.TextField(blank=True)
    profile_picture = CloudinaryField(
        "profile_picture",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.user.username


class Photo(models.Model):
    """
    Represents a photo or artwork displayed in the gallery.
    """

    title = models.CharField(max_length=200)
    description = models.TextField()
    image = CloudinaryField("image")
    tags = models.CharField(max_length=255)
    uploaded_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="photos",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    likes = models.ManyToManyField(
        User,
        related_name="liked_photos",
        blank=True,
    )

    dislikes = models.ManyToManyField(
        User,
        related_name="disliked_photos",
        blank=True,
    )

    def __str__(self):
        return self.title
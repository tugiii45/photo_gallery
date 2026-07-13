from django.contrib import admin
from .models import Profile, Photo


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "bio")
    search_fields = ("user__username", "user__email")


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("title", "uploaded_by", "created_at")
    search_fields = ("title", "description", "tags")
    list_filter = ("created_at",)
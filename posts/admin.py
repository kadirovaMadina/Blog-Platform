from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "description", "photo", "user", "date")
    search_fields = ("user", "title")


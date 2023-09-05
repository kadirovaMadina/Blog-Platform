from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin): 
    list_display = ("pk", "text", "user", "post", "date")
    search_fields = ("user", "post")
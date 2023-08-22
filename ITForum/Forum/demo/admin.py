from django.contrib import admin
from .models import User, Message, Topic, Category


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "categories", "email",
                    "last_login", "is_active", 'created_at']
    list_filter = ["username", "categories", "is_active"]
    search_fields = ['username', 'categories', 'is_active']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ["text", "created_at", "deleted_at"]
    list_filter = ["created_at"]


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ["title"]
    list_filter = ["title"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = ["name"]

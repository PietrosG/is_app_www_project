from django.contrib import admin

# Register your models here.

from .models import Category, Post, Topic

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at", "modified_at"]

admin.site.register(Category)
admin.site.register(Topic)
admin.site.register(Post)
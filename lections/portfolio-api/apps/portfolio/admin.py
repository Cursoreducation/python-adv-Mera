from django.contrib import admin
from apps.portfolio.models import Comment, Image, Portfolio


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("text", "image")


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "portfolio", "created_by")


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "created_by")

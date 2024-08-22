from django.contrib import admin
from .models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "short_description", "slug", "thumbnail")
    fields = ("title", "short_description", "full_description", "slug", "thumbnail")


admin.site.register(BlogPost, BlogPostAdmin)

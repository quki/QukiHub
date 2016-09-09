from django.contrib import admin
from .models import Post, CategoryPost


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "overview", "category", "created")

    fieldsets = [
        ('제목', {'fields': ['title']}),
        ('요약/개요', {'fields': ['overview'], 'classes': ['collapse']}),
        ('내용', {'fields': ['content']}),
        ('카테고리', {'fields': ['category']}),
        (None, {'fields': ['slug', 'publish', 'tags', 'created', 'memo']}),
    ]
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(CategoryPost)

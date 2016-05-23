from django.contrib import admin
from myblog.models import Category
from myblog.models import Post

class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInLine,
    ]
admin.site.register(Category, CategoryAdmin)


class PostAdmin(admin.ModelAdmin):
    inlines = [
        PostInLine,
    ]
admin.site.register(Post, PostAdmin)


class CategoryInLine(CategoryAdmin.TabularInline):
    model = Category


class PostInLine(PostAdmin.TabularInline):
    model = Post


from django.contrib import admin
from myblog.models import Category
from myblog.models import Post


class CategoryAdmin(admin.ModelAdmin):
    inlines = [CategoryInLine]


class PostAdmin(admin.ModelAdmin):
    inlines = [PostInLine]


class CategoryInLine(CategoryAdmin.TabularInline):
    model = Category


class PostInLine(PostAdmin.TabularInline):
    model = Post

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

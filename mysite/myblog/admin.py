from django.contrib import admin
from myblog.models import Category
from myblog.models import Post


class CategoryInLine(admin.TabularInline):
    model = Category.posts.through


class CategoryAdmin(admin.ModelAdmin):
    inlines = [CategoryInLine]
    exclude = ('Category', )


admin.site.register(Post)
admin.site.register(Category, CategoryAdmin)

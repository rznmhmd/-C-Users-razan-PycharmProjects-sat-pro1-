from django.contrib import admin
from .models import Post, Comment, Category

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status',)
    list_filter = ('status',)
    search_fields = ('title', 'content',)


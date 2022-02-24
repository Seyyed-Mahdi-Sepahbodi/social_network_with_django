from django.contrib import admin
from .models import Post, Comment, Like

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'slug', 'updated_at')
    search_fields = ('slug',)
    list_filter = ('updated_at',)
    raw_id_fields = ('user',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'created_at', 'is_reply']
    raw_id_fields = ['user', 'post', 'reply']

admin.site.register(Comment, CommentAdmin)


admin.site.register(Like)

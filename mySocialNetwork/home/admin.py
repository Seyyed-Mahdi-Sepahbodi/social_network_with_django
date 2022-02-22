from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'slug', 'updated_at')
    search_fields = ('slug',)
    list_filter = ('updated_at',)
    raw_id_fields = ('user',)


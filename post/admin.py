from django.contrib import admin
from .models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    fields = ['username', 'content']
    list_display = ['username', 'created_at']

admin.site.register(Post, PostAdmin)
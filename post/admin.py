from django.contrib import admin
from .models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    fields = ['user', 'content']
    list_display = ['user', 'created_at']

admin.site.register(Post, PostAdmin)
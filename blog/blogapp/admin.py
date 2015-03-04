from django.contrib import admin
from blogapp.models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'text', 'pub_date', 'upd_date', 'is_public')

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'pub_date')

admin.site.register(Comment, CommentAdmin)


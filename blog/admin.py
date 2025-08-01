from django.contrib import admin
from .models import Post, Comment, Tag


# Customize the Post admin interface
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'datetime_modified')
    list_filter = ('status', 'datetime_modified')
    search_fields = ('title', 'text')
    ordering = ('-datetime_modified',)
    raw_id_fields = ('author',)


# Customize the Comment admin interface
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'post', 'datetime_created', 'rating')
    list_filter = ('rating', 'datetime_created')
    search_fields = ('author_name', 'text')


# Customize the Tag admin interface
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
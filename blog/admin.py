from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'author','datetime_created','status')
    ordering = ('id',)


# admin.site.register(Post, PostAdmin)

from django.contrib import admin
from .models import *

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    model = Blog
    exclude = ('id',)
    list_display = ['title', 'created_at']


class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ['related_blog', 'body', 'created_at']
    search_fields = ['blog__title']

    def related_blog(self, obj):
        return obj.blog.title
    related_blog.short_description = 'Blog'



admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
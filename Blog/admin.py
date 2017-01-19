from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib import admin

admin.autodiscover()
admin.site.unregister(User)
admin.site.unregister(Group)



# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    model = Blog
    exclude = ('id',)
    list_display = ['title', 'created_at']


class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ['related_blog', 'body', 'created_at']
    fields = ['body']
    search_fields = ['blog__title']

    def related_blog(self, obj):
        return obj.blog.title

    def has_add_permission(self, request, obj=None):
        return False

    related_blog.short_description = 'Blog'


class UserAdmin(admin.ModelAdmin):
    model = User


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)

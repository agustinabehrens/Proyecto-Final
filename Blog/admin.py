from turtle import title
from django.contrib import admin
from . import models
from Blog.models import Avatar

admin.site.register(models.Category)

admin.site.register(Avatar)

@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'status', 'slug', 'author')
    prepopulated_fields = {'slug': ('title',), }



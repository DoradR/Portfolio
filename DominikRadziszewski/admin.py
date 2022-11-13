from django.contrib import admin
from .models import Category, Contact, Post, PicturesOfPost


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['nameOfPost', 'categoryOfPost']
    search_fields = ('nameOfPost', 'categoryOfPost')


@admin.register(PicturesOfPost)
class PicturesOfPostAdmin(admin.ModelAdmin):
    list_display = ['whichPost', ]
    search_fields = ('whichPost', )


admin.site.register(Category)
admin.site.register(Contact)

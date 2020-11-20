from django.contrib import admin
from .models import Post,Image,Comment
from django_summernote.admin import SummernoteModelAdmin





class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    summernote_fields = ('content',)
    prepopulated_fields = {'slug': ('title',)}
  
admin.site.register(Post, PostAdmin)


class ImagemAdmin(admin.ModelAdmin):
    #list_display = ('title', 'slug', 'status','created_on')
    #list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
  
admin.site.register(Image, ImagemAdmin)



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
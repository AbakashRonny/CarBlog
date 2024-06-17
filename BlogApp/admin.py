from django.contrib import admin
from .models import BlogPostModel
# Register your models here.

@admin.register(BlogPostModel)

class BlogPostAdmin(admin.ModelAdmin):
    list_display=['id','blog_title','topic_title','date','image','author','content']
from django.contrib import admin
from .models import BlogType,Blog

@admin.register(BlogType)
class BlogTyprAdmin(admin.ModelAdmin):
    list_display = ('id','type_name')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','blog_type','auther','readed_num','created_time','last_updated_time')

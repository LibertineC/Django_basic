from django.contrib import admin
from .models import Article

# Register your models here
@admin.register(Article)#注册到admin后台
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id","title","content","author","is_deleted","created_time","last_updated_time","readed_num")
    ordering = ("id",)#正序

#admin.site.register(Article,ArticleAdmin)#注册到admin后台

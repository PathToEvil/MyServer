from django.contrib import admin
from website.models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')

admin.site.register(Article, ArticleAdmin)

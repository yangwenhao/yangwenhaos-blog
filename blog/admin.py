from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['title']
    date_hierarchy = 'pub_date'

admin.site.register(Post, PostAdmin)

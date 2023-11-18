from django.contrib import admin
from .models import Category
from .models import Post

# Register your models here.
#For configuration of category admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title","description",'url','image_tag','add_date')
    search_fields = ('title',)
    list_filter = ('title',)

#Configuration of post admin
class PostAdmin(admin.ModelAdmin):
    list_filter = ['title',]
    list_display = ('title','content','cat')
    search_fields = ('title',)
    list_per_page = 50


# Adding the Post and Category to The Admin Panel
admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)

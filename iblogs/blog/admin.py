from django.contrib import admin
from .models import Category
from .models import Post

# Register your models here.

# Adding the Post and Category to The Admin Panel

admin.site.register(Category)
admin.site.register(Post)

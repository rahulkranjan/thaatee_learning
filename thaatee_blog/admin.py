from django.contrib import admin
from thaatee_blog.models import Blog, Rate, SubCategory, Category, Events
# Register your models here.

admin.site.register(Blog)
admin.site.register(Rate)
admin.site.register(SubCategory)
admin.site.register(Category)
admin.site.register(Events)

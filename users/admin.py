from django.contrib import admin
from .models import Role, User,Profile

admin.site.register(Profile)
admin.site.register(Role)
admin.site.register(User)

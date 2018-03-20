from django.contrib import admin

# Register your models here.
from .user import UserModel

admin.site.register(UserModel.Todo)

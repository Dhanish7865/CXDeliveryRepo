from django.contrib import admin
from .models import UserModel

# Register your models here.

#admin.site.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ["last_name", "first_name", "age", "location", "shoe_size"]
    list_filter = ["last_name",]
    fields = [("first_name", "last_name"), "age", "shoe_size", "location"]

admin.site.register(UserModel, UserModelAdmin)
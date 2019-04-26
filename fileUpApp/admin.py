from django.contrib import admin

from fileUpApp.models import UserInfo


# Register your models here.


class UserInfoAdmin(admin.ModelAdmin):
    # lis = ['id', 'userName']
    list_display = ['id', 'userName','idDelete']

admin.site.register(UserInfo, UserInfoAdmin)

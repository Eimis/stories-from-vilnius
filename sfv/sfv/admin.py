from django.contrib import admin
from django_facebook import models
from django.contrib.auth.admin import UserAdmin

class AccountAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'facebook_id')

admin.site.register(models.FacebookCustomUser, AccountAdmin)
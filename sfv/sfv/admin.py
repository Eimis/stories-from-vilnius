from django.contrib import admin
from django_facebook import models
from django.contrib.auth.admin import UserAdmin
from sfv.models import Story

class AccountAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'facebook_id')

class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')

admin.site.register(models.FacebookCustomUser, AccountAdmin)
admin.site.register(Story, StoryAdmin)




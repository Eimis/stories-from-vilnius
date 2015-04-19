from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from sfv.models import Story

class AccountAdmin(UserAdmin):
    list_display = ('id', 'username', 'email')

class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')

# admin.site.register(Story, StoryAdmin)

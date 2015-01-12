from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from models import Profile, Education, Link, School


class EducationInline(admin.StackedInline):
    model = Education


class LinkInline(admin.StackedInline):
    model = Link


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(UserAdmin):
    inlines = (ProfileInline, EducationInline, LinkInline)


class SchoolAdmin(admin.ModelAdmin):
    pass

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(School, SchoolAdmin)

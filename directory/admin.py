from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from import_export import fields, resources, widgets
from import_export.admin import ImportExportMixin, ImportExportModelAdmin

from models import Profile, Education, Link, School


class EducationInline(admin.StackedInline):
    model = Education


class LinkInline(admin.StackedInline):
    model = Link


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class UserResource(resources.ModelResource):
    town_city = fields.Field(attribute='profile__town_city', column_name='town_city', readonly=False)
    state = fields.Field(attribute='profile__state', column_name='state', readonly=False)

    education = fields.Field(attribute='profile__education_set', widget=widgets.ManyToManyWidget)

    def before_import(self, dataset, dry_run):
        print dataset
        print dry_run

    def before_save_instance(self, instance, dry_run):
        print instance

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email')



class UserAdmin(ImportExportMixin, UserAdmin):
    resource_class = UserResource
    inlines = (ProfileInline, EducationInline, LinkInline)


class SchoolResource(resources.ModelResource):
    class Meta:
        model = School
        fields = ('id', 'type', 'name')


class SchoolAdmin(ImportExportModelAdmin):
    resource_class = SchoolResource
    pass


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(School, SchoolAdmin)

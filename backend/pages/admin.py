
from django.contrib import admin
from pages.models import Team, Guide
from import_export.admin import ImportExportModelAdmin, ExportActionMixin
from import_export import resources


# Register your models here.

class GuideResource(resources.ModelResource):
    class Meta:
        model = Guide
        fields = ('name', 'domain_1', 'domain_2', 'domain_3',
                  'email', 'vacancy')


class GuideAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'domain_1', 'domain_2', 'domain_3',
                    'email', 'vacancy')

    resource_class = GuideResource


class TeamResource(resources.ModelResource):
    class Meta:
        model = Team
        fields = ('id', 'project_name', 'no_of_members', 'reg_no_1',
                  'student_1_name', 'student_1_no', 'reg_no_2', 'student_2_name', 'student_2_no')


class TeamAdmin(ImportExportModelAdmin):
    list_display = ('project_name', 'no_of_members', 'reg_no_1',
                    'student_1_name', 'student_1_no', 'reg_no_2', 'student_2_name', 'student_2_no')

    resource_class = TeamResource


admin.site.register(Guide, GuideAdmin)
admin.site.register(Team, TeamAdmin)

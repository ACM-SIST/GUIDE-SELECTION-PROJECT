
from django.contrib import admin
from pages.models import Team, Guide
from import_export.admin import ExportActionMixin


# Register your models here.


class GuideAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('name', 'domain_1', 'domain_2', 'domain_3',
                    'email', 'experience', 'vacancy')


class TeamAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('project_name', 'no_of_members', 'reg_no_1',
                    'student_1_name', 'reg_no_2', 'student_2_name')
    # list_display = ('project_name', 'project_domain', 'project_description', 'no_of_members', 'reg_no_1', 'student_1_name',
    #                 'student_1_email', 'student_1_no',
    #                 'reg_no_2', 'student_2_name', 'student_2_email', 'student_2_no')


admin.site.register(Guide, GuideAdmin)
admin.site.register(Team, TeamAdmin)

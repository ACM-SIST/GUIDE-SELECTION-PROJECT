
from django.contrib import admin
from pages.models import Otp, Otp_Two, Team, Guide, Temp_Team, Temp_User
from import_export.admin import ImportExportModelAdmin, ExportActionMixin
from import_export import resources


# Register your models here.

class GuideResource(resources.ModelResource):
    class Meta:
        model = Guide
        import_id_fields = ('serial_no',)
        exclude = ('id',)
        fields = ('serial_no', 'name', 'emp_id', 'designation', 'domain_1', 'domain_2', 'domain_3',
                  'email', 'myImage', 'vacancy')


class GuideAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('serial_no', 'name', 'emp_id', 'designation', 'domain_1', 'domain_2', 'domain_3',
                    'email', 'myImage', 'vacancy')
    ordering = ('serial_no',)

    resource_class = GuideResource


class TeamResource(resources.ModelResource):
    class Meta:
        model = Team

        fields = ('id', 'teamID', 'project_name', 'no_of_members', 'reg_no_1',
                  'student_1_name', 'student_1_no', 'reg_no_2', 'student_2_name', 'student_2_no', 'reg_no_3', 'student_3_name', 'student_3_no', 'guide', 'guide_email')


class TeamAdmin(ImportExportModelAdmin):
    list_display = ('id', 'teamID', 'project_name', 'no_of_members', 'reg_no_1',
                    'student_1_name', 'student_1_no', 'reg_no_2', 'student_2_name', 'student_2_no', 'guide', 'guide_email')
    ordering = ('teamID',)
    resource_class = TeamResource


class Temp_TeamResource(resources.ModelResource):
    class Meta:
        model = Temp_Team

        fields = ('id', 'teamID', 'project_name', 'no_of_members', 'reg_no_1',
                  'student_1_name', 'student_1_no', 'reg_no_2', 'student_2_name', 'student_2_no', 'reg_no_3', 'student_3_name', 'student_3_no')


class Temp_TeamAdmin(ImportExportModelAdmin):
    list_display = ('id', 'teamID', 'project_name', 'no_of_members', 'reg_no_1',
                    'student_1_name', 'student_1_no', 'reg_no_2', 'student_2_name', 'student_2_no')
    # ordering = ('teamID',)
    resource_class = Temp_TeamResource


admin.site.register(Guide, GuideAdmin)
admin.site.register(Team, TeamAdmin)
# admin.site.register(Team)
admin.site.register(Otp)
admin.site.register(Otp_Two)
admin.site.register(Temp_Team, Temp_TeamAdmin)
admin.site.register(Temp_User)

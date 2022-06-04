
from django.contrib import admin
from django.contrib.auth.models import User
from pages.models import Guide
from import_export.admin import ExportActionMixin


# Register your models here.


class GuideAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('name', 'domain_1', 'domain_2', 'domain_3',
                    'email', 'experience', 'vacancy')


# class UserAdmin(ExportActionMixin, admin.ModelAdmin):
#     list_display = ('username', 'email')


class UserAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('username', 'email')
    actions = ["export_as_csv"]


# admin.site.register(User, UserAdmin)
admin.site.register(Guide, GuideAdmin)

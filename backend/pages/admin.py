from django.contrib import admin

from pages.models import Guide
from import_export.admin import ExportActionMixin


# Register your models here.


class GuideAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('name', 'domain_1', 'domain_2', 'domain_3',
                    'email', 'experience', 'vacancy')


admin.site.register(Guide, GuideAdmin)

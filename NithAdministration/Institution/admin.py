from django.contrib import admin
from .models import Degree,  Subject
from import_export.admin import ImportExportModelAdmin

class ResultAdmin(ImportExportModelAdmin):
    pass
admin.site.register(Degree,ResultAdmin)
admin.site.register(Subject,ResultAdmin)

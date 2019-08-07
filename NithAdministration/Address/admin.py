from django.contrib import admin
from .models import City, District, State, Country
from import_export.admin import ImportExportModelAdmin


class ResultAdmin(ImportExportModelAdmin):
    pass


admin.site.register(City,ResultAdmin)
admin.site.register(District,ResultAdmin)
admin.site.register(State,ResultAdmin)
admin.site.register(Country,ResultAdmin)

from django.contrib import admin
from cap.models import CampusAmbassador
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(CampusAmbassador)
class CampusAmbassadorAdmin(ImportExportModelAdmin):
    pass
from django.contrib import admin
from .models import ManagementTeamRecs, WebTeamRecs, MediaTeamRecs
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(ManagementTeamRecs)
class ManagementTeamRecsAdmin(ImportExportModelAdmin):
    pass

@admin.register(MediaTeamRecs)
class MediaTeamRecsAdmin(ImportExportModelAdmin):
    pass

@admin.register(WebTeamRecs)
class WebTeamRecsAdmin(ImportExportModelAdmin):
    pass
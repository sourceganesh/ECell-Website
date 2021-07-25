from django.contrib import admin
from .models import ManagementTeamRecs, WebTeamRecs, MediaTeamRecs
# Register your models here.

admin.site.register(ManagementTeamRecs)
admin.site.register(MediaTeamRecs)
admin.site.register(WebTeamRecs)
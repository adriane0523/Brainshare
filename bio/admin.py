from django.contrib import admin
from django.db import models
# Register your models here.
from bio.models import Co_Investigators, Co_Principal_Investigators, Project_Personnel, Advisory_Comitee

class Co_InvestigatorsAdmin(admin.ModelAdmin):
    list_display = ["name"]

class  Co_Principal_InvestigatorsAdmin(admin.ModelAdmin):
    list_display = ["name"]
class Project_PersonnelAdmin(admin.ModelAdmin):
    list_display = ["name"]
class  Advisory_ComiteeAdmin(admin.ModelAdmin):
    list_display = ["name"]


admin.site.register(Co_Investigators, Co_InvestigatorsAdmin)
admin.site.register(Co_Principal_Investigators, Co_Principal_InvestigatorsAdmin)
admin.site.register(Project_Personnel, Project_PersonnelAdmin)
admin.site.register(Advisory_Comitee, Advisory_ComiteeAdmin)

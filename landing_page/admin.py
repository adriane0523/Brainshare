from django.contrib import admin
from django.db import models
# Register your models here.
from landing_page.models import Sulton_links


class sulstonLinksAdmin(admin.ModelAdmin):
    pass

admin.site.register(Sulton_links, sulstonLinksAdmin)


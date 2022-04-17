from django.contrib import admin
from django.db import models
# Register your models here.
from resources.models import File, Resource_page, Post, Bookmarks, Related_projects, Publications, PatientStories


class FileAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']


class ResourceIndexAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']


class PostAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']


class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['post']
    '''
    fieldsets = (
        ("Title", {
            'fields': ['title', 'description']
        }),
        ('Quiz Content', {
            'fields': [ 'content']
        }),
         ('Connect connect page to course', {
            'fields': ['courses']
        }),
    )
    '''


class PublicationsAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']


class Related_projectsAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']


class PatientStoriesAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']

admin.site.register(Publications, PublicationsAdmin)
admin.site.register(Related_projects, Related_projectsAdmin)
admin.site.register(Bookmarks, BookmarkAdmin)
admin.site.register(File, FileAdmin)
admin.site.register(Resource_page, ResourceIndexAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PatientStories, PatientStoriesAdmin)

from django.db import models
import uuid
from django.contrib.flatpages.models import FlatPage
from django import forms
from ckeditor_uploader.fields import RichTextUploadingField
from django import forms
from django.core.files.storage import FileSystemStorage
from sulstonProject.settings import STATIC_ROOT


upload_storage = FileSystemStorage(location=STATIC_ROOT)

class File(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=500)
    description = models.CharField(max_length=1200, default="")


class Resource_page(models.Model):
    title = models.CharField(max_length=255)
    link = models.TextField()
    description = models.CharField(max_length=1200, default="")
    index = models.IntegerField()

    def __str__(self):
        return 'White Paper: ' + self.title

    class Meta:
        # Add verbose name
        verbose_name = 'White Paper'


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = RichTextUploadingField(blank=True)
    presentation_link = models.TextField(blank=True)
    show_presentation_link = models.BooleanField(default=False)
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=True)
    view = models.BooleanField(default=False)
    order = models.IntegerField(default=0)

    def __str__(self):
        return 'Case Studies: ' + self.title

    class Meta:
        # Add verbose name
        verbose_name = 'Case Studies'


class PatientStories(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    picture = models.ImageField(upload_to="",  storage=upload_storage, default = 'none')
    article_title = models.CharField(default="",max_length=255)
    content = RichTextUploadingField(blank=True)
    presentation_link = models.TextField(blank=True)
    show_presentation_link = models.BooleanField(default=False)
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=True)
    view = models.BooleanField(default=False)
    order = models.IntegerField(default=0)

    def __str__(self):
        return 'Patient Stories: ' + self.title

    class Meta:
        # Add verbose name
        verbose_name = 'Patient Stories'


class Bookmarks(models.Model):
    title = models.CharField(max_length=255)
    html_id = models.CharField(max_length=255)
    post = models.ManyToManyField(Post)

    def __str__(self):
        return 'Bookmarks: ' + self.title

    class Meta:
        # Add verbose name
        verbose_name = 'Boookmark'


class Related_projects(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255, blank=True)
    description = models.TextField()

    def __str__(self):
        return 'Related Project: ' + self.title

    class Meta:
        verbose_name = 'Related Project'
        # Add verbose name


class Publications(models.Model):
    title = models.CharField(max_length=255, blank=True)
    link = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)

    published_date = models.CharField(max_length=255, blank=True)
    author = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return 'Publications: ' + self.title

    class Meta:
        verbose_name = 'Publication'
        # Add verbose name

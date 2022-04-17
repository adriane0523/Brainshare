from django.db import models

# Create your models here.
class Sulton_links(models.Model):
    title = models.CharField(max_length=255, blank=True)
    link = models.TextField( blank=True)
    description = models.TextField(blank=True)

    
    def __str__(self):
        return 'Sulston Links: ' + self.title

    class Meta: 
        verbose_name = 'Sulston-links' 
        # Add verbose name 
from django.db import models

# Create your models here.
class Urlshortner(models.Model):
    original_url = models.URLField(max_length=900, blank=True)
    new_url = models.CharField(max_length=80, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Urlshortner: {self.original_url}"
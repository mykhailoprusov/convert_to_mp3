from django.db import models
from django.utils import timezone

class Video(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='convert_to_mp3/video')
    
    date_posted = models.DateTimeField(default=timezone.now)

class Audio(models.Model):
    file = models.FileField()


    def __str__(self):
        return self.file.name
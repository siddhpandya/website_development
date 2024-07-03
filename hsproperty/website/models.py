from django.db import models

class MediaUpload(models.Model):
    video = models.FileField(upload_to='videos/')
    ppt = models.FileField(upload_to='ppts/')
    latitude = models.DecimalField(max_digits=18, decimal_places=15)
    longitude = models.DecimalField(max_digits=18, decimal_places=15)
    details = models.TextField(default='No details provided')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.latitude}, {self.longitude} - {self.uploaded_at}"

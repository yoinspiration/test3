from django.db import models

class File(models.Model):
    # file = models.FileField(upload_to='')
    file = models.FileField(upload_to='uploads/')
    upload_time = models.DateTimeField(auto_now_add=True)

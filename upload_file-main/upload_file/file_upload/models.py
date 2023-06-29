from django.db import models

# Create your models here.

class UploadFiles(models.Model):
    name = models.CharField(max_length=50)
    my_file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.name
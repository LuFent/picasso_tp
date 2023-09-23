from django.db import models
from django.utils.timezone import now
from os.path import basename


class File(models.Model):
    file = models.FileField(upload_to="uploaded_files/")
    uploaded_at = models.DateTimeField(default=now)
    processed = models.BooleanField(default=False)

    def __str__(self):
        return f"File {basename(self.file.path)}"
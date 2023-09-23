from django.db.models.signals import post_delete
from .models import File
from django.dispatch import receiver
import os
from django.conf import settings


@receiver(post_delete, sender=File)
def delete_file(sender, instance, **kwargs):
    try:
        os.remove(instance.file.path)
    except Exception:
        pass
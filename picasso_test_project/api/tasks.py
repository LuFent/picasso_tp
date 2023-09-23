from picasso_test_project.celery import app
from .models import File
from .tools import process_image


@app.task
def process_file(file_id):
    file = File.objects.get(id=file_id)
    try:
        process_image(file.file.path)
    except Exception:
        pass
    file.processed = True
    file.save()
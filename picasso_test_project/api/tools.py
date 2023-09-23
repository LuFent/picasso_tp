from PIL import Image
from os.path import join
from django.conf import settings

RESIZE_VALUES = (1127, 710)
PASTE_VALUES = (175, 177)

def process_image(file_path):

    with Image.open(join(settings.BASE_DIR, "api", "file_processing", "frame.jpg")) as frame:
        frame.load()

    with Image.open(file_path) as img:
        img.load()

    frame.paste(img.convert("L").resize(RESIZE_VALUES), PASTE_VALUES)

    frame.save(file_path)
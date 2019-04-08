#picture_handler.py
import os
from PIL import Image
from flask import url_for, current_app


def add_report(rep_upload):
    filename = rep_upload.filename
    storage_filename = filename.split('.')[-1]
    # storage_filename = str(username)+'.'+ext_type
    filepath = os.path.join(current_app.root_path, 'static//report_folder', storage_filename)
    pic.save(filepath)
    return storage_filename

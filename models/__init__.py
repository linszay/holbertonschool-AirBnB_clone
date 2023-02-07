#!/usr/bin/python3
from models.engine.file_storage import FileStorage
from models import base_model
from models.base_model import BaseModel
"""creating a unique FileStorage instance"""


storage = FileStorage()
storage.reload()

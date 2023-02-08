#!/usr/bin/python3
from models.base_model import BaseModel
"""creating review class that inherits from BaseClass"""


class Review(BaseModel):
    """review class"""
    place_id = ""
    user_id = ""
    text = ""

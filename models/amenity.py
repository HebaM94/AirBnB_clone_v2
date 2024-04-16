#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class defining Amenity"""
    def __init__(
            self,
            name="",
            *args,
            **kwargs):
        """New Amenity instance"""
        super().__init__(**kwargs)
        self.name = name

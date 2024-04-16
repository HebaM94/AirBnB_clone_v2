#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel


class City(BaseModel):
    """ The city class, contains state ID and name """
    def __init__(
            self,
            state_id="",
            name="",
            *args,
            **kwargs):
        """New City instance"""
        super().__init__(**kwargs)
        self.state_id = state_id
        self.name = name

#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    def __init__(
            self,
            name="",
            *args,
            **kwargs):
        """New State instance"""
        super().__init__(**kwargs)
        self.name = name

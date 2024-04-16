#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class defining a user"""
    def __init__(
            self, email="",
            password="",
            first_name="",
            last_name="",
            *args,
            **kwargs):
        """New User instance"""
        super().__init__(**kwargs)
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="delete", backref="state")
    else:
        name = ""

    def __init__(self, *args,**kwargs):
        """New State instance"""
        super().__init__(**kwargs)

    if os.getenv("HBNB_TYPE_STORAGE") != "db":

        @property
        def cities(self):
            """getter attribute cities that returns the list of City instances
            with state_id equals to the current State.id"""
            from models import storage
            cts = []
            cities = storage.all("City")
            for city in cities.values():
                if city.state_id == self.id:
                    cts.append(city)
            return cts

   

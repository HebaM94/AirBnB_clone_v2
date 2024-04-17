#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="delete", backref="states")

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        name=""
        @property
        def cities(self):
            """getter attribute cities that returns the list of City instances
            with state_id equals to the current State.id"""
            from models import storage
            cts = []
            cities = storage.all("City").values()
            for city in cities:
                if city.state_id == self.id:
                    cts.append(city)
            return cts

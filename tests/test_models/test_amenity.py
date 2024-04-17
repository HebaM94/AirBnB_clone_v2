#!/usr/bin/python3
"""Amenity"""
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.base_model import BaseModel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """Testing Amenity class"""

    def setUp(self):
        """Set up test environment"""
        self.model = Amenity()
        self.name_attr = "name"

    def test_inheritance(self):
        """Testing if Amenity inherits from BaseModel"""
        super().test_inheritance(Amenity)

    def test_attributes(self):
        """Testing attributes"""
        super().test_attributes()
        self.assertTrue(hasattr(self.model, 'name'))
        self.assertEqual(self.model.name, '')

    def test_attribute_types(self):
        """Testing types of attributes"""
        super().test_attribute_types()
        self.assertIsInstance(self.model.name, str)

    def test_str_representation(self):
        """Testing __str__ method"""
        super().test_str_representation("[Amenity] ({}) {}".format(
            self.model.id, self.model.__dict__))

    def test_to_dict_method(self):
        """Testing to_dict method"""
        super().test_to_dict_method("Amenity")

    def test_initialization(self):
        """Testing if attributes are initialized"""
        super().test_initialization()
        new_amenity = Amenity(name="test_name")
        self.assertEqual(new_amenity.name, "test_name")


if __name__ == '__main__':
    unittest.main()
